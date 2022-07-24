<template>
<div class ="login-background">
  <div class="login-profile-sign-in-page">
          <nuxt-link to="/"><h1 id = "title-sign-in-page">Studielabbet</h1></nuxt-link>
          <!-- <nuxt-link to="/SignUp"><h1 id = "about">Om oss</h1></nuxt-link>
          <nuxt-link to="/SignUp"><h1 id = "about">Kontakt</h1></nuxt-link> -->
    </div>
    <div class = "row-justify-content-center">
      <v-card elevation="10" width="100rem" class="elevation-4 text-left" shaped color="black">
        <v-card-title>Skapa nytt konto</v-card-title>
        <v-card-text>
          <v-form>
            <v-text-field
              label="Namn"
              name="name"
              prepend-icon="mdi-account"
              type="text"
              required
              autofocus
              v-model="form.name"
            ></v-text-field>

            <v-text-field
              label="Email"
              prepend-icon="mdi-email"
              id="email"
              type="email"
              class="form-control"
              name="email"
              value
              required
              autofocus
              v-model="form.email"
            ></v-text-field>

            <v-text-field
              label="Mobilnummer"
              prepend-icon="mdi-cellphone"
              id="phone"
              type="phone"
              class="form-control"
              name="phone"
              value
              required
              autofocus
              v-model="form.phone"
            ></v-text-field>

            <v-text-field
              label="Lösenord"
              prepend-icon="mdi-lock"
              id="password"
              type="password"
              class="form-control"
              name="password"
              value
              required
              autofocus
              v-model="form.password"
            ></v-text-field>
            

          </v-form>
        </v-card-text>
        <v-card-actions align="center" class="text-center" >
          
          <div class="form-group row mb-0">
            <div class="register-btn">
                <v-btn type="submit" class="btn btn-primary" @click="submit" depressed large
                  >Registrera</v-btn
                >
            </div>
          </div>

        </v-card-actions>
        <v-card-subtitle id = "new" align="center">Redan medlem? <nuxt-link to="/LoggedInContent/PersonalPage">Logga in</nuxt-link></v-card-subtitle>
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
//https://firebase.google.com/docs/auth/web/manage-users
export default {
    
  data() {
    return {
      form: {
        name: "",
        email: "",
        password: "",
        phone:"",
      },
      error: null
    };
  },
  methods: {
    async submit() {
      await $nuxt.$fire
        .auth.createUserWithEmailAndPassword(this.form.email, this.form.password).then(data => {
          data.user
            .updateProfile({
              displayName: this.form.name
            })
            .then(() => {
              
              const uid = this.$fire.auth.currentUser.uid
              const username = this.$fire.auth.currentUser.displayName
              const email = this.$fire.auth.currentUser.email
              const phone = this.$fire.auth.currentUser.phone
              const data_to_send = {uid,username,email,phone}
              console.log(data_to_send)

              // data = {uid,username,email}

                  //we need to set axios create with "withCredential: true" in order
                  //for session to work.Has to do with cookie compability
              const ip = axios.create({withCredentials: true})
            
              ip.post('http://localhost:8050/register_activity',data_to_send ).then(response =>{return this.ip = response.data})
              console.log(ip)
               
            });
        })
        .catch(err => {
          this.error = err.message;
        });
    },


  },
};
</script>

<style>

.container-sign-up{
  background-image: linear-gradient(to right, #8fadf4, #4c1cac);
  display:flex;
  justify-content: center;
  /* position:absolute; */
  width:100vw;
  height: 100vh;
  /* margin-left:5rem; */
}

.row-justify-content-center{
  background-color: rgb(255, 255, 255);
  width: 24vw;
  height:33vh;
  margin-top:20vh;
  border-radius: 20px 20px;
  

}

</style>