<template>
    <div class="songs">
        <h1>Songs</h1>
        <Player v-bind:currentSong="currentSong" v-bind:songs="songs"/>
        <div v-bind:key="song.id" v-for="song in songs">
            <SongItem v-bind:song="song" v-on:play-sound="playSound"/>
        </div>
        
    </div>
</template>

<script>
import SongItem from "./SongItem";
import Player from "./Player";

export default {
    name: "Songs",
    components: { SongItem, Player },
    props: ["songs", "currentSong"],
    methods: { 
    playSound(song){ 
        let oSongs = this.songs.filter(temp => temp.id != song.id)
        oSongs.forEach(function(oSong){
            if(oSong.isPlaying){
                oSong.song.pause();
                oSong.isPlaying = false;
            }
            oSong.song = new Audio(oSong.urlSong);
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