<template>
  <div class ="container">
    <Headertwo/>
    <CardsContainer/>
    <BarContainer/>
    <FooterView/>
  </div>
 
</template>

<script>

import CardsContainer from '../components/CardsHomePage/CardsContainer.vue';
import BarContainer from '../components/InfoSections/BarContainer.vue';
import Headertwo from '~/components/Headertwo.vue';
import FooterView from '../components/InfoSections/FooterView.vue'
export default { components: {CardsContainer, BarContainer ,Headertwo, FooterView } }
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
