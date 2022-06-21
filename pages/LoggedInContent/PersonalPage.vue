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


    </div>


    
</template>

<script>

import { getDatabase, ref, set, child, get } from "firebase/database";
import { getAuth, deleteUser } from "firebase/auth";
    export default {

        middleware: 'auth', //We can definie middleware at each page, instead of setting it
        //globally in nuxt.config

        data(){
            return{

                grade: "",
                data: {}

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
                grade = this.grade 
                this.data = grade
                const db = getDatabase();
                set(ref(db, 'users/' + $nuxt.$fire.auth.currentUser.uid), {
                    username: "Cecilias",
                    email: "c@gmail.com",
                    betyg: grade,
                    id: $nuxt.$fire.auth.currentUser.uid
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
            }
            
        }

    }
  

</script>

<style lang="scss" scoped>

</style>