<template>
    <div id = "container-side-bar-search">
        <div class="text-analyze-card-search">
            <h1 id = "analyze-title-search">Hitta drömutbildningen du inte visste fanns</h1>
            <p id="analyze-text-search">
            I Sverige finns 16 universitet och 31 högskolor som tillsammans erbjuder över 3 100 olika utbildningsprogram. Inte konstigt att det är svårt att hitta rätt utbildning!
            <br>
            <br>
            Vi har utvecklat ett unikt sökverktyg som gör det enkelt för dig att hitta drömutbildningen du inte visste fanns. Du kan exempelvis filtrera på examen, utbildningens namn och skolor. Eller varför inte filtrera fram alla utbildningar som du har störst chans att komma in på? 
            Du kanske bara vill visa de utbildningar som du är behörig till att söka, eller de som ligger närmast där du bor? Varför inte kombinera alla!?
            Oavsett vad du väljer, så har du en karta till din hjälp som gör att du enkelt kan hålla koll på vart i landet dina favoritutbildningar finns. Om du vill veta mer om en specifik skola eller utbildning är det
            bara att klicka vidare.

            </p>
        </div>

        <div class = "img-analyze-card-search">
            <img src="~/assets/images/map.png" width=90% height=100% >
        </div>


    </div>
</template>

<script>
import VScrollin from "vue-scrollin";

    export default {
     
    }
</script>

<style>

.img-analyze-card-search{
    /* margin-top: 2rem; */
}

#container-side-bar-search{
    display: flex;
    flex-direction: row;
    position:absolute;
    /* margin-top:180vh; */
    /* margin-left:-2rem; */
    padding: 2rem;
    /* background-color: #f4f9e9; */
    width: 90vw;
    margin-top:175px;
    margin-left: 50px;


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

.text-analyze-card-search{
    order: 2;
    display: flex;
    flex-direction: column;
    /* justify-content: flex-end; */
    width:70%;
    flex-wrap: wrap;
    padding: 2rem;
    animation: slide-up 3s;
    
}

#analyze-text-search{
    font-size: 1.3rem;
}

#analyze-title-search{
    margin-bottom: 1.6rem;
}


</style>