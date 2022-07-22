<template>
    <div class="card-container-bar">

        <div> <SideBarAnalyze/></div>
        <div> <SideBarSearch/></div>
        <div> <SideBarCalc/></div>
        <div> <SideBarCalc/></div>
        <div><SideBarAi/></div>
       
    
    </div>
</template>

<script>
import SideBarAnalyze from './SideBarAnalyze.vue'
import SideBarSearch from './SideBarSearch.vue'
import SideBarCalc from './SideBarCalc.vue'
import SideBarGoals from './SideBarGoals.vue'
import SideBarAi from './SideBarAi.vue'
    export default {
  components: { SideBarAnalyze, SideBarSearch, SideBarCalc, SideBarGoals, SideBarAi },
        
    }
</script>

<style>

.card-container-bar{
    position: relative;
    /* margin-top: -10rem; */
    /* background-color: chocolate;
     */
    margin-top: 5rem;
    display: flex;
    flex-direction: column;
    /* align-items: space-evenly; */
    flex-wrap:wrap;
    justify-content: space-evenly;
    gap: 600px 500px;
    z-index: 10;
    /* margin: 1rem; */
    /* margin-top: 4rem; */
    /* padding-left: 20rem; */
    /* padding:1rem; */
    flex-wrap: wrap;
    /* width : 100vw;  
    margin-left:-1rem; */
    /* margin-left: 2rem; */


}

</style>