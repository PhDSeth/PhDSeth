<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-md-8">
        <div class="card">
          <div class="card-header">Register</div>
          <div class="card-body">
            <div v-if="error" class="alert alert-danger">{{error}}</div>
            <form action="#" @submit.prevent="submit">
              <div class="form-group row">
                <label for="name" class="col-md-4 col-form-label text-md-right">Name</label>

                <div class="col-md-6">
                  <input
                    id="name"
                    type="name"
                    class="form-control"
                    name="name"
                    value
                    required
                    autofocus
                    v-model="form.name"
                  />
                </div>
              </div>

              <div class="form-group row">
                <label for="email" class="col-md-4 col-form-label text-md-right">Email</label>

                <div class="col-md-6">
                  <input
                    id="email"
                    type="email"
                    class="form-control"
                    name="email"
                    value
                    required
                    autofocus
                    v-model="form.email"
                  />
                </div>
              </div>

              <div class="form-group row">
                <label for="password" class="col-md-4 col-form-label text-md-right">Password</label>

                <div class="col-md-6">
                  <input
                    id="password"
                    type="password"
                    class="form-control"
                    name="password"
                    required
                    v-model="form.password"
                  />
                </div>
              </div>

              <div class="form-group row mb-0">
                <div class="col-md-8 offset-md-4">
                  <button type="submit" class="btn btn-primary">Register</button>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
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
        password: ""
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
              const data_to_send = {uid,username,email}
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