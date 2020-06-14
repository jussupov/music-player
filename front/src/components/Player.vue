<template>
    <div class="player">
        <h1>{{this.currentSong.title ? `Now Playing: ${this.currentSong.title}` : 'Play music'}}</h1>
    </div>
</template>

<script>

export default {
    name: "Player",
    props: ["currentSong", "songs"]
}

</script>