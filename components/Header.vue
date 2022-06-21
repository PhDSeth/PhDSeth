<template>
    <div class="header">
        <h1 id = "titel-hemsida">Studieverket</h1>
        <!-- <h2>{{$nuxt.$fire.auth.currentUser.email}}</h2> -->
        <h2></h2>
         <nuxt-link to="/SignUp">Om oss</nuxt-link>
         <nuxt-link to="/LoggedInContent/PersonalPage">pROFIL</nuxt-link>
    </div>
</template>

<script>
    export default {
        
    }
</script>

<style>


.header{
    background-color: rgb(21, 32, 57);
    height: 4rem;
    margin-left: -1rem;
    width: 100vw;
    margin-top: -10rem;
    display: flex;
    padding: 0.7rem;
    position: fixed;
    z-index: 2;
    overflow:hidden


}

#titel-hemsida{
    color:rgb(237, 115, 115);
    margin-left: 2rem;
}

</style>