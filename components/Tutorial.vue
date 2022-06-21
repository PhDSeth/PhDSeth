<template>
    <div class = "welcome">
        <h1>Välkommen till studieverket!</h1>

        <div id ="rolling-text">
            <vue-typed-js :strings="['Kommer jag in?', 'Hur stora är mina chanser?', 'Vilken utbildning passar mig?', 
            'Är jag behörig?', 'Vad tycker tidigare studenter?', 'lugn..', 'Vi hjälper dig!']" :loop="true" typeSpeed=9 backSpeed=9 backDelay=2000 startDelay=3000>
            <h3 class="typing"></h3>
            </vue-typed-js>
        </div>

        <div class="additional-info">
                Här finns allt du behöver inför ansökan till universitet & högskolor.
                Låt våra smarta funktioner & kraftfulla verktyg hjälpa dig!
        </div>
        
    </div>
</template>

<script>

import Vue from 'vue'
import VueTypedJs from 'vue-typed-js'
Vue.use(VueTypedJs)

    export default {

        
    }
</script>

<style>

#rolling-text{
      position:absolute;
      top: 6rem;
      font-size: 1.7rem;
  
}
.welcome{
    position: relative;
    margin-top: 10rem;
    display: flex;
    flex-direction: column;
    align-items: center;

}

.additional-info{
    font-size: 1.5rem;
    margin-top:8rem;
}

</style>