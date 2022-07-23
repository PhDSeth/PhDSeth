<template>
    <div id = "container-side-bar-ai">
        <div class="text-analyze-card-ai">
            <h1 id = "analyze-title-ai">Ta reda på dina chanser att bli antagen till din drömutbildning!</h1>
            <p id="analyze-text-ai">
            Är du placerad som reserv i urval 1 eller 2 och undrar om du kommer in? Vi har sammanställt data för landets samtliga utbildningar. Vi kan ge dig svaret på hur stora dina chanser är att bli antagen om du placerats som reserv efter urval 1 och 2. 

            Är du nyfiken på hur stora chanser du har att bli antagen till din drömutbildning? Sluta gissa! Vi har utvecklat ett kraftfullt verktyg baserat på artificiell intelligens som kan ge dig en kvalificerad hint på hur stora chanser du har. Flashback, släng dig i väggen.

            <br>
            <br>
            Funktionen inkluderar:
            </p>
        </div>

        <div class = "img-analyze-card-ai">
            <img src="~/assets/images/circle-info.png" width=90% height=100% >
        </div>


    </div>
</template>

<script>
import VScrollin from "vue-scrollin";

    export default {
     
    }
</script>

<style>

.img-analyze-card-ai{
    margin-top: 2rem;
}

#container-side-bar-ai{
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    position:absolute;
    /* margin-top:110vh; */
    /* margin-left:-2rem; */
    padding: 2rem;
    /* background-color: #f4f9e9; */

    width: 90vw;
    margin-left:60px;
    margin-top:675px;
    background-image: linear-gradient(to right, #f1f5fe, #d9d7e2);
    /* border: solid; */
    /* border-color: #4a4d84; */
    border-radius: 0.4rem;


}

/* @keyframes slide-up {
  from {
    opacity: 0.2;
    transform: translateY(600px);

  }
  to{
    opacity:1;
    transform: translateY(20px);
  }
} */


a{
    text-decoration:none;
}

.text-analyze-card-ai{
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    width:50%;
    flex-wrap: wrap;
    padding: 2rem;
    animation: slide-up 3s;
    
}

#analyze-text-ai{
    font-size: 1.3rem;
}

#analyze-title-ai{
    margin-bottom: 1.6rem;
}


</style>