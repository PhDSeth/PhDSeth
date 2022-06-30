<template>
  <v-row align="center" justify="center">
    <v-col cols="12" sm="8" md="4" align="center">
      <v-card width="500" class="elevation-4 text-left" shaped color="yellow">
        <v-card-title>Login</v-card-title>
        <v-card-subtitle>Login to your dashboard</v-card-subtitle>
        <v-card-text>
          <v-form>
            <v-text-field
              label="Login"
              name="login"
              prepend-icon="mdi-account"
              type="text"
              v-model="auth.email"
            ></v-text-field>

            <v-text-field
              label="Password"
              name="password"
              prepend-icon="mdi-lock"
              type="password"
              v-model="auth.password"
            ></v-text-field>
          </v-form>
        </v-card-text>
        <v-card-actions class="text-center">
          <v-btn
            class="login-button"
            @click="login"
            depressed
            large
            >Login</v-btn
          >
          <v-btn class="reset-button" @click="forgotPassword" depressed large
            >Forgot Password</v-btn
          >
        </v-card-actions>
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
    </v-col>
  </v-row>
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
        that.snackbarText = 'reset link sent to ' + that.auth.email
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

</style>