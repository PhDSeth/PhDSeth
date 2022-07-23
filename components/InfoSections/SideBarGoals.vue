<template>
    <div id = "container-side-bar-goals">
        <div class="text-analyze-card">
            <h1 id = "analyze-title">Bibehåll motivationen genom att sätt upp mål och följa din egna utveckling!</h1>
            <p id="analyze-text">
           Vi vet hur lätt det är att tappa motivationen under studietiden. Genom att följa dina prestationer och lättare få en överblick över dina resultat blir det enklare att bibehålla motovationen.

            Om du verkligen vill in 
            Med våra funktioner kan du följa din betygsutveckling
            Om jag får B istället för D i Svenska 2, hur mycket påverkas mitt betygsnitt? Vilka kurser ska jag välja för att bli behörig till att söka läkarprogrammet?

            Du kanske vill få notiser om när det är dags att ansöka till högskolan? Eller när anmälan till högskoleprovet öppnar?

            <br>
            <br>
            Funktionen inkluderar:
            <br>
            <br>
            <ul>
                <li>Få notiser via sms eller mail när det är dags att anmäla sig till högskoleprovet, söka in till universitet och universitet och högskola. Du kan också få
                    notiser när det är urval 1 och 2 har kommit </li>
                <li></li>
            </ul>


           
            </p>
        </div>

        <div class = "img-analyze-card">
            <img src="~/assets/images/circle-info.png" width=90% height=500px >
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

#container-side-bar-goals{
    display: flex;
    flex-direction: row;
    position:absolute;
    /* margin-top:110vh; */
    /* margin-left:-2rem; */
    padding: 2rem;
    /* background-color: #f4f9e9; */
    margin-top:325px;
    margin-left:80px;
    width: 90vw;
    margin-left:60px;

    /* border-color: #4a4d84; */
    border-radius: 0.4rem;


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
    order:2;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    width:60%;
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