<template>
    <div class="body">

          <div id="top">
        </div>

        <div class="login-profile">
                <nuxt-link to="/SignUp"><h1 id = "about">Om oss</h1></nuxt-link>
                <nuxt-link to="/SignUp"><h1 id = "about">Kontakt</h1></nuxt-link>
                <div class = "profile">
                    <font-awesome-icon id="icon-user" fa-6x :icon="['fa', 'user']" style="font-size: 1rem"/>
                    <nuxt-link to="/LoggedInContent/PersonalPage"><h1 id = "my-profile">Logga in</h1></nuxt-link>
                </div>
          </div>
         
        <div class="header">


            <div class="title-container">
            <nuxt-link to="/"><h1 id = "title">Studielabbet</h1></nuxt-link>
            </div>

            <div id ="rolling-text">
                <vue-typed-js :strings="['Kommer jag in som reserv?', 'Hur stora är mina chanser?','Räcker mina betyg?', 'Vilken utbildning passar mig?', 
                'Är jag behörig?','lugn..', 'Vi på Studielabbet hjälper dig!']" :loop="true" :typeSpeed="40" :backSpeed="40" :backDelay="3000" :startDelay="4000">
                <h3 class="typing"></h3>
                </vue-typed-js>
            </div>

            <div class ="additional-text">
                 <p>Vi har utvecklat 5 unika och kraftfulla verktyg som underlättar livet för dig som blivande student. Läs mer genom att trycka på funktionerna nedan, eller
                  scrolla ner så berättar vi mer!
                 </p>
            </div>

            <div class="kommer-jag-in-btn">
                
            <div id="container">
                <button class="learn-more">
                    <span class="circle" aria-hidden="true">
                    <span class="icon arrow"></span>
                    </span>
                    <span class="button-text"> Skapa ett konto</span>
                   
                </button>

          
                 
                </div>
            </div>
            <div class="arrow-container">
                <a href="#" v-scroll-to="{ element: '#element', duration: 2000 }"><div class="arrow-down"></div></a>
            </div>

                        

        </div>

        <client-only>
          <div v-show="isVisible" class="scrollup-button" @click="scrollToTop">
            <img src="~/assets/images/to-top.png" alt="back to top" />
  
          </div>
        </client-only>

        <div id="element">
            .
        </div>





   

 

    
        <!-- <h2>{{$nuxt.$fire.auth.currentUser.email}}</h2> -->

    </div>
</template>

<script>
import { debounce } from 'vue-debounce'
import Vue from 'vue'
import VueTypedJs from 'vue-typed-js'
// import BackToTop from 'vue-backtotop'
Vue.use(VueTypedJs)
// import Vue from 'vue'
// import BackToTop from 'vue-backtotop'

// Vue.use(BackToTop)

    export default {
      data() {
    return {
      scrollTop: null,
      isVisible: false,
      visibleDistance: 200,
    }
  },
  mounted() {
    window.addEventListener('scroll', debounce(this.scrollListener, 100), true)
  },
  beforeDestroy() {
    window.removeEventListener('scroll', this.scrollListener)
  },
  methods: {
    scrollListener() {
      if (window.pageYOffset) {
        this.scrollTop = window.pageYOffset
      } else {
        this.scrollTop = 0
      }
      
      if (this.scrollTop > this.visibleDistance) {
        this.isVisible = true
      } else {
        this.isVisible = false
      }
    },
    scrollToTop() {
      this.intervalId = setInterval(() => {
        if (window.pageYOffset === 0) {
          clearInterval(this.intervalId)
        }
        window.scroll(0, window.pageYOffset - 30)
      }, 4)
    },
  },
        
    }
</script>

<style lang="scss">

@import url('https://fonts.googleapis.com/css2?family=Rubik+Mono+One&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Anton&family=Rubik+Mono+One&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Anton&family=Lato:wght@700&family=Poppins:wght@400;900&family=Rubik+Mono+One&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Anton&family=Lato:wght@300;700&family=Poppins:wght@400;900&family=Rubik+Mono+One&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Anton&family=Lato:wght@300;700&family=Montserrat:wght@500&family=Poppins:wght@400;900&family=Rubik+Mono+One&display=swap');
/* font-family: 'Anton', sans-serif;
font-family: 'Lato', sans-serif;
font-family: 'Poppins', sans-serif;
font-family: 'Rubik Mono One', sans-serif; */


.scrollup-button {
  position: fixed;
  bottom: 3rem;
  right: 2rem;
  cursor: pointer;
  // border-radius: 0.25rem;
  opacity: 0.5;
  padding: 0.7rem;
  z-index: 100000;
  transition: opacity 0.15s ease;
  &:hover {
    opacity: 1;
  }
  img {
    width: 2.3rem;
    height: 2.3rem;
  }
}


#element{

  position:absolute;
  margin-top: 140px;
  color:white;
  
  
}

// .top-button{
//   position:fixed;
//   background-color: #ffffff;
//   z-index:10000000000000;
//   right: 2vw;
//   border:solid;
//   border-radius: 10rem;
//   border-color: #5436cb;
//   height:3rem;
//   width:3rem;
//   // width: 2rem;
//   // right:-5vw;
//   margin-top:14vh;
//     // --offset: 10px; 

//   // margin-top: calc(100vh + var(--offset));
// }


#rolling-text{
      position:absolute;
      display:flex;
      flex-wrap: wrap;
      color: rgb(0, 0, 0);
    //   background-color: #dce2db;
    //   background-color: #f4f9e9;
    //   background-color: #2968fa;
    //   background-image: linear-gradient(to right, #2968fa, #0d93e7);
      margin-top:30vh;
      font-size: 2rem;
      font-family: 'Lato', sans-serif;
      margin-left: 2rem;
      text-align: center;

}

.typing{
    // color:#000;
    color:rgb(255, 255, 255);
}

.additional-text{
      position:absolute;
      display:flex;
      flex-wrap: wrap;
      //   color: rgb(0, 0, 0);
      margin-top:40vh;
      padding: 0.5rem;
      // font-size: 2rem;
      font-family: 'Lato', sans-serif;
      justify-content: center;
     
      text-align: center;
    
}

.additional-text{
    color:rgb(253, 253, 253);
    font-size: 1.4rem;
    width: 55vw;
    text-align:center;
}

.header{
    display:flex;
    flex-direction: row;
    /* background-image: url("~assets/images/background.svg"); */
    height: 80vh;
    width:100vw;
    // background-color: rgb(221, 232, 233);
    // background-color: #dce2db;
    // background-color: #eef5db;
    // background-color: #7bb9e6;
    margin-top: -2rem;
    margin-left:-1rem;
    /* margin-top: -10rem; */
    /* display: flex; */
    /* padding: 0.7rem; */
    z-index: 200;
    overflow:hidden;
    justify-content: center;
    // border-radius: 1rem 30rem; 
    background-image: linear-gradient(to right, #8dacf4, #602cca);
    
    
    /* flex-direction: row;
    justify-content: space-between; */
    /* margin-bottom: 10rem; */

}

.title-container{
     margin-top: 15vh;
}

#title:hover{
      font-size: 3.7vw;
}

#title{
    color:rgb(255, 255, 255);
    /* margin-top: 2rem; */
    position:relative;
    font-size: 3.5vw;
    margin-left: 3rem;
    // font-family: 'Anton', sans-serif;
    font-family: 'Montserrat', sans-serif; 
   
}

p{
  font-family: 'Montserrat', sans-serif;
}

h1{
  font-family: 'Montserrat', sans-serif;
}

h3{
  font-family: 'Montserrat', sans-serif;
}

.login-profile{
    background-image: linear-gradient(to right, #8dacf4, #602cca);
    display: flex;
    flex-direction: row;
    position: fixed;
    // background-color: #f35730;
    width:100vw;
    margin-left:-1rem;
    // right:0;
    justify-content: space-evenly;
    
    // padding: 2rem;
    margin-top: -1.9rem;
    /* background-color: aliceblue; */
    // background-color: #add7f6;
    z-index: 1000;
    // opacity: 0.90;
    
    }

 #icon-user{
    // margin-left:1rem;
 }

#about{
    color: rgb(255, 255, 255);
    margin-top: 3rem;
    font-size: 1.6rem;
}

.profile{
    display:flex ;
    flex-direction: column;
    align-items: center;
    color: rgb(255, 255, 255);
    margin-top: 2rem;
    // font-size: 1.6rem;
}

#my-profile{
    color:rgb(255, 255, 255);
    font-size: 1.6rem;
}



#title-2{
    color:rgb(232, 232, 232);
    /* margin-top: 4rem; */
    /* margin-left: 3rem; */
    position:relative;
    font-size: 1.2vw;
    /* margin-bottom: -2rem; */
    font-family: 'Anton', sans-serif;

}

.kommer-jag-in-btn{
    color:white;
    position:absolute;
    border: white;
    margin-top:52vh;
    margin-left: 1rem;
}



@media only screen and (min-width: 1025px) {
.header {
background-position:initial;
}
}



@import url('https://fonts.googleapis.com/css?family=Mukta:700');

$bg: #f3f8fa;
$white: #fff;
// $black: #f35730;
$black: #de7732;

@mixin transition($property: all, $duration: 0.45s, $ease: cubic-bezier(0.65,0,.076,1)) {
  transition: $property $duration $ease;
}

* {
  box-sizing: border-box;
  &::before, &::after {
    box-sizing: border-box;
  }
}

body {
  font-family: 'Mukta', sans-serif;
  font-size: 1rem;
  line-height: 1.5;
//   display: flex;
//   align-items: center;
//   justify-content: center;
  margin: 0;
  min-height: 100vh;
  background: $bg;
}

button {
  position: relative;
  display: inline-block;
  cursor: pointer;
  outline: none;
  border: 0;
  vertical-align: middle;
  text-decoration: none;
  background: transparent;
  padding: 0;
  margin-left:1rem;
  font-size: inherit;
  font-family: inherit;
  &.learn-more {
    width: 12rem;
    height: auto;
    .circle {
      @include transition(all, 0.45s, cubic-bezier(0.65,0,.076,1));
      position: relative;
      display: block;
      margin: 0;
      margin-left: -0.4rem;
      width: 3rem;
      height: 3rem;
      background: $black;
      border-radius: 1.625rem;
      .icon {
        @include transition(all, 0.45s, cubic-bezier(0.65,0,.076,1));
        position: absolute;
        top: 0;
        bottom: 0;
        margin: auto;
        background: $white;
        &.arrow {
          @include transition(all, 0.45s, cubic-bezier(0.65,0,.076,1));
          left: 0.625rem;
          width: 1.125rem;
          height: 0.125rem;
          background: none;
          &::before {
            position: absolute;
            content: '';
            top: -0.25rem;
            right: 0.0625rem;
            width: 0.625rem;
            height: 0.625rem;
            border-top: 0.125rem solid #fff;
            border-right: 0.125rem solid #fff;
            transform: rotate(45deg);
          }
        }
      }
    }
    .button-text {
      @include transition(all, 0.45s, cubic-bezier(0.65,0,.076,1));
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      padding: 0.75rem 0;
      margin: 0 0 0 1.85rem;
      color: $black;
      font-weight: 700;
      line-height: 1.6;
      text-align: center;
      text-transform: uppercase;
    }
  }
  &:hover {
    .circle {
      width: 100%;
      .icon {
        &.arrow {
        background: $white;
        transform: translate(1rem, 0);
        }
      }
    }
    .button-text {
      color: $white;
    }
  }
}

@supports (display: grid) {
  body {
    display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-gap: 0.625rem;
  grid-template-areas: ". main main ." ". main main .";
  }
  
  #container {
    grid-area: main;
    align-self: center;
    justify-self: center;
    padding:2.2rem;
  }
}



.arrow-container {
  width: 30px;
  /* cubic-bezier-easing = sine / mehr Beispiele: https://easings.net/ */
  animation: bounce 1600ms infinite cubic-bezier(0.445, 0.05, 0.55, 0.95);
  cursor: pointer;
  height: 15px;
  position:absolute;
  top: 95vh;
  z-index:500;
}

.arrow-down {
  height: 6px;
  background: #5436cb;
  transform: rotate(45deg);
  transform-origin: 0% 0%;
  border-radius: 5px;

}
.arrow-down:after {
  content: '';
  position: absolute;
  width: 100%;
  height: 100%;
  bottom: 0;
  left: 100%;
  border-radius: 5px;
  background: #5436cb;
  transform: rotate(-90deg);
  transform-origin: 0% 100%;
}

@keyframes bounce {
50% {
    transform: translateY(-15px);
  }
}




// scroll-bar-----------------------
::-webkit-scrollbar {
  width: 20px;
}

/* Track */
::-webkit-scrollbar-track {
  box-shadow: inset 0 0 5px grey; 
  border-radius: 10px;
}
 
/* Handle */
::-webkit-scrollbar-thumb {
  background: rgb(255, 255, 255); 
  border:solid;
  border-block-color: black;
  border-radius: 10px;
}

/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
  background: #000000; 
}


#about, #my-profile ,#title {
  --s: 0.1em;   /* the thickness of the line */
//   --c: #b34c4c; /* the color */
  --c: #ffffff;
  color: white;
  padding-bottom: var(--s);
  background: 
    linear-gradient(90deg,var(--c) 50%,#000 0) calc(100% - var(--_p,0%))/200% 100%,
    linear-gradient(var(--c) 0 0) 0% 100%/var(--_p,0%) var(--s) no-repeat;
  -webkit-background-clip: text,padding-box;
          background-clip: text,padding-box;
  transition: 0.5s;
}
#about:hover , #my-profile:hover {
  --_p: 100%
}







</style>