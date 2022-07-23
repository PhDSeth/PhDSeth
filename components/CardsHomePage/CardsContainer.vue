<template>
    <div class="card-container">

        <div> <AnalyzeCard/></div>
        <div> <SearchCard/></div>
        <div> <CalcCard/></div>
        <div> <GoalsCard/></div>
        <div><AiCard/></div>
       
    
    </div>
</template>

<script>
import AnalyzeCard from './AnalyzeCard.vue'
import SearchCard from './SearchCard.vue'
import CalcCard from './CalcCard.vue'
import GoalsCard from './GoalsCard.vue'
import AiCard from './AiCard.vue'
    export default {
  components: { AnalyzeCard, SearchCard, CalcCard, GoalsCard, AiCard },
        
    }
</script>

<style>

.card-container{
    position: relative;
    /* margin-top: -10rem; */
    /* background-color: chocolate;
     */
    margin-top: -5rem;
    display: flex;
    align-items: center;
    flex-wrap:wrap;
    justify-content: space-around;
    gap: 1px;
    z-index: 10;
    /* margin: 1rem; */
    /* margin-top: 4rem; */
    /* padding-left: 20rem; */
    /* padding:1rem; */
    flex-wrap: wrap;
    width : 100vw;  
    margin-left:-1rem;
    /* margin-left: 2rem; */


}

</style>