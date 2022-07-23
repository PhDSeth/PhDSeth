<template>

    <div id = "container-side-bar-analyze">
        <div class="text-analyze-card-analyze">
            <h1 id = "analyze-title-analyze">Analysera dina styrkor & svagheter</h1>
            <p id="analyze-text-analyze">
            Inom vilka ämnesområden presterar du bäst? Inom vilka områden är du lite svagare? Du kanske vill hitta en utbildning som bäst matchar mot din profil? Eller behöver du tips på vilka kurser du bör 
            plugga upp? Med denna funktionen får du en överblick över dina prestationer. 
            <br>
            <br>
            Oavsett vad du behöver hjälp med så finns vi där för dig. Allt du behöver göra är att lägga in dina betyg. Det kan du göra smidigt genom att klippa och klistra. Busenkelt!
            

            <br>
            <br>
            Funktionen inkluderar:
            <ul class = "list-analyze">
                <li > <font-awesome-icon id="icon-check-analyze" fa-6x :icon="['fa', 'circle-check']" style="font-size: 1.3rem"/>Automatisk analys av dina styrkeområden</li>
                <li> <font-awesome-icon id="icon-check-analyze" fa-6x :icon="['fa', 'circle-check']" style="font-size: 1.3rem"/>Förslag på kurser att plugga upp för att optimera dina chanser att bli antagen</li>

            </ul>
            </p>
        </div>

        <div class = "img-analyze-card-analyze">
            <img src="~/assets/images/circle-info.png" width=80% height=80% >
        </div>


    </div>

</template>

<script>
import VScrollin from "vue-scrollin";

    export default {
     
    }
</script>

<style>


#icon-check-analyze{
    margin-right:0.8rem;
}

.img-analyze-card-analyze{
    margin-top: 2rem;
}

#container-side-bar-analyze{
    display: flex;
    flex-direction: row;
    position:absolute;
    /* margin-top:110vh; */
    /* margin-left:-2rem; */
    padding: 2rem;
    /* background-color: #f4f9e9; */
    width: 90vw;
    margin-left:60px;
    margin-top:50px;
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

.text-analyze-card-analyze{
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    width:60%;
    flex-wrap: wrap;
    padding: 2rem;
    animation: slide-up 3s;
    
}

#analyze-text-analyze{
    font-size: 1.3rem;
}

#analyze-title-analyze{
    margin-bottom: 1.6rem;
}

.list-analyze{
    margin-left:3rem;
    list-style: none;
}

p{
    
}

</style>