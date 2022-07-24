<template>
<div class ="login-background">
  <div class="login-profile-sign-in-page">
          <nuxt-link to="/"><h1 id = "title-sign-in-page">Studielabbet</h1></nuxt-link>
          <!-- <nuxt-link to="/SignUp"><h1 id = "about">Om oss</h1></nuxt-link>
          <nuxt-link to="/SignUp"><h1 id = "about">Kontakt</h1></nuxt-link> -->
    </div>
    <div class = "login-card">
      <v-card elevation="10" width="100rem" class="elevation-4 text-left" shaped color="black">
        <v-card-title>Logga in till Studielabbet</v-card-title>
        <v-card-text>
          <v-form>
            <v-text-field
              label="Logga in"
              name="login"
              prepend-icon="mdi-account"
              type="text"
              v-model="auth.email"
            ></v-text-field>

            <v-text-field
              label="Lösenord"
              name="password"
              prepend-icon="mdi-lock"
              type="password"
              v-model="auth.password"
            ></v-text-field>
          </v-form>
        </v-card-text>
        <v-card-actions align="center" class="text-center" >
          <v-btn
            class="login-button"
            @click="login"
            depressed
            large
            color=""
            >Logga in</v-btn
          >
          <v-btn class="reset-button" @click="forgotPassword" depressed large
            >Glömt lösenord</v-btn
          >
        </v-card-actions>
        <v-card-subtitle id = "new" align="center">Ny på Studielabbet? <nuxt-link to="/SignUp">Skapa konto</nuxt-link></v-card-subtitle>
      </v-card>
      <v-snackbar
        :timeout="4000"
        v-model="snackbar"
        absolute
        bottom
        center
      >
        {{ snackbarText }}
      </v-snackbar>
</div>
</div>
</template>

<script>
import axios from 'axios'
export default {
  
  data() {
    return {
      snackbar: false,
      snackbarText: 'No error message',
      auth: {
        email: '',
        password: ''
      }
    }
  },
  methods: {
    async login() {
      let that = this
      try{
      await this.$fire.auth.signInWithEmailAndPassword(this.auth.email, this.auth.password).then(()=>
      {
          const uid = this.$fire.auth.currentUser.uid
          const username = this.$fire.auth.currentUser.displayName
          const email = this.$fire.auth.currentUser.email
          const data_to_send = {uid,username,email}
          console.log(data_to_send)
          
          const ip = axios.create({withCredentials: true})


          ip.post('http://localhost:8050/register_activity',data_to_send ).then(response =>{return this.ip = response.data})
      

      })
      this.$router.push('/')
      
      }
      catch(error){
        that.snackbarText = error.message
        that.snackbar = true
      }
    },
    async forgotPassword() {
      let that = this
      await this.$fire.auth.sendPasswordResetEmail(this.auth.email)
      .then(function (){
        that.snackbarText = 'Vi har skickat ett mail till ' + that.auth.email
        that.snackbar = true
      })
      .catch(function (error) {
        that.snackbarText = error.message
        that.snackbar = true
      })
    }
  }
}
</script>

<style>

#new{
  display:flex;
  flex-direction:column;
}

.login-background{
  position: absolute;
  background-image: linear-gradient(to right, #8fadf4, #4c1cac);
  height: 100vh;
  width: 100vw;
  display:flex;
  justify-content: center;
}

.login-card{
  margin-top:20vh;
  width: 24vw;
}



#title-sign-in-page{
    color: rgb(255, 255, 255);
    margin-top: 3rem;
    font-size: 1.6rem;
}

.login-profile-sign-in-page{
    background-image: linear-gradient(to right, #8fadf4, #4c1cac);
    display: flex;
    flex-direction: row;
    position: fixed;
    width:100vw;
    margin-left:-1rem;
    justify-content: space-evenly;
    margin-top: -1.9rem;
    z-index: 1000;
    
    }

#title-sign-in-page:hover{
      font-size: 1.7rem;
}

</style>

