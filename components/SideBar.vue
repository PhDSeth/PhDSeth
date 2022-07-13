<template>
    <div class = "container-side-bar">
        <div id="edu-of-week">
            <h2>Veckans utbildning</h2>
            <h3>Läkarprogrammet</h3>
            <h3>300 HP</h3>
        </div>

        <div id="common-quest">
            <nuxt-link to="https://nuxtjs.org">Vanliga frågor</nuxt-link>
        </div>

        <div id="about-us">
            <nuxt-link to="/PersonalPage">Om oss</nuxt-link>
        </div>

        <div id="contact-us">
            <nuxt-link to="https://nuxtjs.org">Kontakta oss</nuxt-link>
        </div>

        <div id="follow-us">
            <nuxt-link to="https://nuxtjs.org">Kontakta oss</nuxt-link>
        </div>


    </div>
</template>

<script>
    export default {
        
    }
</script>

<style>
.container-side-bar{
    background-color: #1F354C;
    position:fixed;
    display:flex;
    flex-direction: column;
    align-items: center;
    align-content: center;
    justify-content: center;
    right:0rem;
    width: 20vw;
    height:100vh;   
    top:0rem; 
   
}

a{
    text-decoration:none;
}




</style>