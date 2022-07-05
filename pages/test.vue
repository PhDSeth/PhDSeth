<template>
    <div>
        <button @click="writeUserData">HEJ</button>
    </div>
</template>

<script>

import { getDatabase, ref, set } from "firebase/database";
    export default {


methods:{

//https://firebase.google.com/docs/database/web/read-and-write
//  writeUserData() {
//   const db = getDatabase();
//   set(ref(db, 'users/' + "12"), {
//     username: "Cecilias",
//     email: "c@gmail.com",
//   });
// },

}
    }
</script>

<style lang="scss" scoped>

</style>