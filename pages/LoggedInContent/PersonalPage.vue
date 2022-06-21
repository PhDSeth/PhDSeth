<template>
    <div>
        {{$nuxt.$fire.auth.currentUser.email}} ÄR INLOGGAD! 
        <button @click="signOut">Logga ut</button>

        <div>
            <label for="grade">Betyg</label>
            <input type="text" id="grade_input" v-model="grade">
            <h3>{{grade}}</h3>
            <button @click="writeUserData(grade)">Submit</button>
        </div>


    </div>


    
</template>

<script>

import { getDatabase, ref, set } from "firebase/database";
    export default {

        middleware: 'auth', //We can definie middleware at each page, instead of setting it
        //globally in nuxt.config

        data(){
            return{

                grade: ""

            }
        },

        methods:{
            signOut(){
                $nuxt.$fire.auth.signOut()
            },

             writeUserData(grade) {
                grade = this.grade 
                const db = getDatabase();
                set(ref(db, 'users/' + grade), {
                    username: "Cecilias",
                    email: "c@gmail.com",
                    betyg: grade
  });
},
        }

    }
  

</script>

<style lang="scss" scoped>

</style>