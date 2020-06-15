<template>
  <div id="app">
      <div class="bg-image" :style="fullCover"></div>
      <div class="container">
          <Songs v-bind:songs="songs" v-bind:currentSong="currentSong" v-on:set-current-song="setcurrentSong" v-bind:time="time"/>
      </div>
  </div>
</template>

<script>

import Songs from "./components/Songs";
import axios from "axios";

export default {
  name: 'App',
  components: {
    Songs
  },
  data(){
    return {
      songs: [],
      currentSong: {}
    }
  },
  created(){
    axios.get('http://localhost:5000/api/songs/')
      .then(res => {
        let temp = res.data;
        for (let i=0; i<temp.length;i++){
          temp[i].isPlaying=false;
          temp[i].urlSong = temp[i].song;
          temp[i].song = new Audio(temp[i].song);

        }
        this.songs = temp;
        }
      )
      .catch(err => console.log(err));
  },
  methods: {
    setcurrentSong(song){
      this.currentSong = song;
      let x = this;
      this.currentSong.song.ontimeupdate = function(){
        x.generateTime();
      }

    },
    generateTime(){
      let width = (100 / this.currentSong.song.duration) * this.currentSong.song.currentTime;
      this.time = this.currentSong.song.currentTime;
      this.barWidth = `${width}%`;
    }
  },
  computed: {
    fullCover(){
      var style = {
        'z-index':'-1',
        'width': '100%',
        'height': '100vh',
        'background-position':'center',
        'background-size':'cover',
        'background-repeat': 'no-repeat',
        '-webkit-filter': 'blur(12px)'
      }
      if (this.currentSong.cover){
        style.backgroundImage = `url('${this.currentSong.cover}')`;
      }
      else{
        style.backgroundImage = "url('https://m.media-amazon.com/images/G/01/digital/music/merch/2019/LandingPages/katana/subtest/Katana_Aquisition_Desktop_1_1x.jpg')";
      }
      return style;
    }
  }
}
</script>

<style>
* {
  padding: 0;
  margin: 0;
  font-family: Ubuntu, sans-serif;
}



#app{
  width: 100%;
  height: 100%;
}

body{
  background-color: black;
}

.container{
  position: absolute;
  z-index: 2;
  background-color: white;
  width: 500px;
  margin-left: auto;
  margin-right: auto;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
</style>
