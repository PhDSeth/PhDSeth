<template>
    <div class = "container-side-bar">
        <div class="text-analyze-card">
            <h1 id = "analyze-title">Analysera dina styrkor & svagheter</h1>
            <p id="analyze-text">
            Inom vilka ämnesområden presterar du bäst? Inom vilka områden är du lite svagare? Du kanske vill hitta en utbildning som bäst matchar mot din profil? Eller behöver du tips på vilka kurser du bör 
            plugga upp?
            <br>
            <br>
            Oavsett vad du behöver hjälp med så finns vi där för dig. Allt du behöver göra är att lägga in dina betyg. Det kan du göra smidigt genom att klippa och klistra. Busenkelt!
            </p>
        </div>

        <div class = "img-analyze-card">
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

.img-analyze-card{
    margin-top: 2rem;
}

.container-side-bar{
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    position:absolute;
    /* margin-top:110vh; */
    /* margin-left:-2rem; */
    padding: 2rem;
    /* background-color: #f4f9e9; */
    width: 100vw;


}

@keyframes slide-up {
  from {
    opacity: 0.2;
    transform: translateY(600px);

  }
  to{
    opacity:1;
    transform: translateY(20px);
  }
}


a{
    text-decoration:none;
}

.text-analyze-card{
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    width:50%;
    flex-wrap: wrap;
    padding: 2rem;
    animation: slide-up 3s;
    
}

#analyze-text{
    font-size: 1.3rem;
}

#analyze-title{
    margin-bottom: 1.6rem;
}


</style>