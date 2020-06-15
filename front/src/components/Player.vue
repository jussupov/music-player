<template>
    <div class="player">

        <div v-if="this.currentSong.title">
            <div :style="playerActive" class="info">
                <p class='info-text'>Now playing</p>
                <p class='info-track'><span>{{this.currentSong.artist}}</span> - {{this.currentSong.title}}</p>
            </div>
            


        </div>
        <div v-else>
            <div class="playerDisable"></div>
        </div>
    </div>
</template>

<script>

export default {
    name: "Player",
    props: ["currentSong", "songs", "time"],
    computed: {
        playerActive(){
            return {
                'background-image':`linear-gradient(180deg, rgba(0,0,0,0.4) 0%, rgba(255,255,255,0) 50%, rgba(0,0,0,0.4) 100%), url('${this.currentSong.cover}')`,
                'width':'100%',
                'height':'500px',
                'background-size':'cover',
                'background-position': 'center'
            }
        }
    },
    data(){
        return {seek: 0};
    },
    methods: {
        generateTime(){
            let width = (100 / this.currentSong.song.duration) * this.currentSong.song.currentTime;
            this.barWidth = `${width}%`;
            console.log(this.barWidth);
        }
    },
    created() {
        if(this.currentSong.song){
            this.currentSong.song.ontimeupdate = function(){
                this.generateTime();
            }
        }
    }
}

</script>

<style scoped>
.player{
    height: 500px; 
}

.info{
    color: white;
    text-align: center;
    padding-top: 3%;
    padding-bottom: 3%;
}

.info-text{
    font-weight: bold;
}

.info-track span{
    font-weight: 500;
}

.playerDisable{
    background-image: url('https://is5-ssl.mzstatic.com/image/thumb/Purple113/v4/1e/e1/3f/1ee13f07-ecdf-f8ad-1e6b-815fae9772cc/source/0x0ss-85.png');
    width: 100%;
    height: 500px;
    background-size: cover;
    background-position: center;
}

</style>