<template>
        <div class="song" v-bind:class="{'active':song.isPlaying}">
            <div v-if="song.isPlaying" class="btn">
                <img class="btn" src="http://127.0.0.1:5000/media/pause.svg" width="32" height="32" alt="" @click="$emit('play-sound', song)">

            </div>
            <div v-else class="btn">
                <img class="btn" src="http://127.0.0.1:5000/media/play.svg" width="32" height="32" alt="" @click="$emit('play-sound', song)">
            </div>
            
            <div class="cover">
                <img v-bind:src='song.cover' alt="" width="100px" height="100px">
            </div>
            <div class="info">
                <h1 class="title" style="font-size: 20px;">
                    {{song.title}}
                </h1>
                <p style="font-size: 20px;">{{song.artist}}</p>
            </div>
            
        </div>
        
</template>

<script>

export default {
    name: "SongItem",
    props: ["song"],
}
</script>


<style scoped>

.song{
    display: flex;
    align-items: center;
    width: 100%;
    background-color: white;
}

.active{
    background-color: #f1f1f1;
}

.cover{
    margin-right: 20px;
}

.btnPlayPause{
    padding: 1.2em 2em;
    background: linear-gradient(135deg, #6e8efb, #a777e3);

}

.btn{
    margin-right: 3%;
    margin-left:3%
}


</style>