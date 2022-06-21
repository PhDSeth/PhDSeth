<template>
    <div class="header">
        <nuxt-link to="/"><h1 id = "title">Studieverket</h1></nuxt-link>
        <!-- <h2>{{$nuxt.$fire.auth.currentUser.email}}</h2> -->
        <div class="login-profile">
         <nuxt-link to="/SignUp"><h1 id = "about">Skapa konto</h1></nuxt-link>
         <div class = "profile">
            <font-awesome-icon id="icon-user" fa-6x :icon="['fa', 'user']" style="font-size: 1rem"/>
            <nuxt-link to="/LoggedInContent/PersonalPage"><h1 id = "profile">Min profil</h1></nuxt-link>
         </div>
        </div>
    </div>
</template>

<script>
    export default {
        
    }
</script>

<style>


.header{
    background-color: rgb(21, 32, 57);
    height: 8rem;
    width: 100vw;
    margin-top: -10rem;
    display: flex;
    padding: 0.7rem;
    position: fixed;
    z-index: 2;
    overflow:hidden;
    flex-direction: row;
    justify-content: space-between;
}

.login-profile{
    display: flex;
    flex-direction: row;
    position: relative;
    width:40rem;
    justify-content: space-evenly;
    margin-top: 1rem;
    /* background-color: aliceblue; */
    
    }

#icon-user{
    color:aliceblue;
}

#about{
    color: whitesmoke;
    margin-top: 3rem;
    font-size: 1.6rem;
}

#profile{
    color: whitesmoke;
    margin-top: 3rem;
    font-size: 1.6rem;
}

#title{
    color:rgb(237, 115, 115);
    margin-top: 2rem;
    margin-left: 2rem;
    font-size: 3rem;
}

</style>