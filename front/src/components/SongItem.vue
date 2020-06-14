<template>
        <div class="song" v-bind:class="{'zz':song.isPlaying}">

            <button @click="$emit('play-sound', song)">
                {{ song.isPlaying ? 'Pause' : 'Play'}}
            </button>
            <div class="cover">
                <img v-bind:src='song.cover' alt="" width="100px" height="100px">
            </div>
            <div class="info">
                <h1 class="title">
                    {{song.title}}
                </h1>
                <p>{{song.artist}}</p>
                <p>{{song.isPlaying}}</p>
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
}

.zz{
    background-color: red;
}

.cover{
    margin-right: 20px;
}


</style>