<template>
  <div>
    <Header/>
    <SideBar/>
    <Tutorial/>
    <CardsContainer/>
  </div>
 
</template>

<script>

import Tutorial from '~/components/Tutorial.vue';
import CardsContainer from '../components/CardsContainer.vue';
import Header from '~/components/Header.vue';
import SideBar from '../components/SideBar.vue';
export default { components: { Tutorial, CardsContainer, Header, SideBar } }
</script>

<style>

/* body{
  display: flex;
  align-self: right;

} */

</style>
