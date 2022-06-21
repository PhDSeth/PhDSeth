<template>
    <div class="card-container">
        <AnalyzeCard/>
        <SearchCard/>
        <CalcCard/>
        <GoalsCard/>
        <AiCard/>
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
    display: flex;
    align-items: center;
    justify-content: space-around;
    margin-top: 4rem;
    padding-left: 20rem;
    padding-right: 20rem;


}

</style>