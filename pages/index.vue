<template>
  <div class ="container">
    <Headertwo/>
    <!-- <SideBar/> -->
    <CardsContainer/>
  </div>
 
</template>

<script>

import CardsContainer from '../components/CardsHomePage/CardsContainer.vue';
import SideBar from '../components/SideBar.vue';
import Headertwo from '~/components/Headertwo.vue';
export default { components: {CardsContainer, SideBar, Headertwo } }
</script>

<style>

/* body{
  display: flex;
  align-self: right;

} */

.container{
  position: relative;
  display: flex;
  flex-direction: column;
  /* justify-content: center; */
  align-items:left;
}

</style>
