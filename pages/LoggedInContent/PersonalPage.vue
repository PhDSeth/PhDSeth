<template>
    <div>
        {{$nuxt.$fire.auth.currentUser.email}} ÄR INLOGGAD! 
        <button @click="signOut">Logga ut</button>

        <div>
            <label for="grade">Betyg</label>
            <input type="text" id="grade_input" v-model="grade">
            <h3>{{grade}}</h3>
            <button @click="writeUserData(grade)">Submit</button>
            <button @click="deleteUser()">Radera konto</button>
            <h2>{{data}}</h2>
        </div>
   

        <iframe src="http://localhost:8050/dash/" width=700 height=600 onload="rrr"></iframe>
        <button @click= "sendGrades">Skicka iväg</button>
        <h4>{{ip}}</h4>
        



    </div>


    
</template>

<script>

import { getDatabase, ref, set, child, get } from "firebase/database";
import { getAuth, deleteUser } from "firebase/auth";
import axios from 'axios'

    export default {
        modules: ['vue-iframes/nuxt'],

        middleware: 'auth', //We can definie middleware at each page, instead of setting it
        //globally in nuxt.config
        components: {
            
        },

        data(){
            return{

                grade: "",
                data: {},
                ip: ''

            }
        },

        mounted(){ //created can also work, but then we will have a little delay, since created executes AFTER
        //components is created, while mounter is executed BEFORE components is created
            const b =  $nuxt.$fire.auth.currentUser.uid
            console.log("B ÄR:", b)
                const dbRef = ref(getDatabase());
                    get(child(dbRef, `users/${b}`)).then((snapshot) => {
                    if (snapshot.exists()) {
                        this.data = snapshot.val().betyg
                        console.log(snapshot.val());
                    } else {
                        console.log("No data available");
                    }
                    }).catch((error) => {
                    console.error(error);
                    });
        },

        methods:{
            signOut(){
                $nuxt.$fire.auth.signOut()
            },

             writeUserData(grade) {
                console.log(this.$fire.auth.currentUser)
                grade = this.grade 
                this.data = grade
                const db = getDatabase();
                set(ref(db, 'users/' + this.$fire.auth.currentUser.uid), {
                    username: this.$fire.auth.currentUser.displayName,
                    email: this.$fire.auth.currentUser.email,
                    betyg: grade,
                    id: this.$fire.auth.currentUser.uid
            });
            },

            deleteUser(){
                const auth = getAuth();
                const user = auth.currentUser;

                deleteUser(user).then(() => {
                    console.log(snapshot.val())
                
                }).catch((error) => {
                // An error ocurred
                // ...
                });
            },

            async sendGrades(){

                const ip = await axios.get('http://localhost:8050').then((response) =>{
                    return this.ip = response
                })
               



            }

   
            
        },
        

    }
  

</script>

<style lang="scss" scoped>

</style>