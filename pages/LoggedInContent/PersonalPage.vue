<template>
    <div>
        {{$nuxt.$fire.auth.currentUser.email}} ÄR INLOGGAD! 
        <button @click="signOut">Logga ut</button>
        <nuxt-link to="/Test">TILL TEST</nuxt-link>

        <div>
            <label for="grade">Betyg</label>
            <input type="text" id="grade_input" v-model="grade">
            <h3>{{grade}}</h3>
            <button @click="writeUserData(grade)">Submit</button>
            <button @click="deleteUser()">Radera konto</button>
            <h2>{{data}}</h2>
        </div>
   

        <iframe src="http://localhost:8050/dash/" width=700 height=600 onload="rrr"></iframe>
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

        methods:{
            signOut(){
                $nuxt.$fire.auth.signOut().then(()=>{
                    const uid = this.$fire.auth.currentUser.uid
                    const username = this.$fire.auth.currentUser.displayName
                    const email = this.$fire.auth.currentUser.email
                    const data_to_send = {uid,username,email}
                    const ip = axios.create({withCredentials: true})

                    ip.post('http://localhost:8050/logout',data_to_send ).then(response =>{return this.ip = response.data})

                })
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
      
                    const ip = this.$axios.$get('http://localhost:8050/delete_account')
                    this.ip = ip
                    console.log(snapshot.val())
                
                }).catch((error) => {
                // An error ocurred
                // ...
                });
            },

   
            
        },

    }
  

</script>

<style lang="scss" scoped>

</style>