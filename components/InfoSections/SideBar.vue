<template>
    <div class = "container-side-bar">
        <div class="text-analyze-card">
            <h1 id = "analyze-title">Analysera dina styrkor & svagheter</h1>
            <p id="analyze-text">
            Med våra smarta verktyg analyserar vi dina betyg & presenterar för dig dina styrkor & svagheter. Inom vilka områden presterar du bäst? Inom vilka områden är du lite svagare? Du kanske vill hitta en utbildning som bäst matchar mot din profil?

            Behöver du hjälp att plugga upp betyg inför din ansökan till universitetet? Låt oss berätta för dig vilka kurser du borde plugga upp, allt för att maximera dina chanser att bli antagen.
            Allt du behöver göra är att lägga in dina betyg. Det kan du göra genom att klippa och klistra. Busenkelt!

            </p>
        </div>

        <div class = "img-analyze-card">
            <h4>cfgvhbjnkm</h4>
        </div>


    </div>
</template>

<script>

  import VScrollin from "vue-scrollin";
    export default {
        
        
    }
</script>

<style>
.container-side-bar{
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    position:absolute;
    margin-top:110vh;
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