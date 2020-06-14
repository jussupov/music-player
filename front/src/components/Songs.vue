<template>
    <div class="songs">
        <h1>Songs</h1>
        <div class="player">

            {{this.currentSong.title ? `Now Playing: ${this.currentSong.title}` : 'Play music'}}
        </div>
        <div v-bind:key="song.id" v-for="song in songs">
            <SongItem v-bind:song="song" v-on:play-sound="playSound"/>
        </div>
        
    </div>
</template>

<script>
import SongItem from "./SongItem";

export default {
    name: "Songs",
    components: { SongItem },
    props: ["songs", "currentSong"],
    methods: { 
    playSound(song){ 
        let oSongs = this.songs.filter(temp => temp.id != song.id)
        oSongs.forEach(function(oSong){
            if(oSong.isPlaying){
                oSong.song.pause();
                oSong.isPlaying = false;
            }
        });
        if (song.isPlaying){
            song.song.pause();
            song.isPlaying = false;
            this.$emit('set-current-song', {})
        }else{
            song.song.play();
            song.isPlaying = true;
            this.$emit('set-current-song', song)
        }

        } 
    }
    
}
</script>


<style scoped>
    .songs{
        display: block;
    }
</style>