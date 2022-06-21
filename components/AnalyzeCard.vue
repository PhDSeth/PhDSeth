<template>
    <div class = "card" >

        <div id="description">
            <div id = container>
                <h5>Analyser dina styrkor & svagheter</h5>
                <div id="image-styrkor"> <img src="~/assets/images/styrkor.png" width=40% height=40% ></div>
            </div>
           
        </div>

        

    </div>
</template>

<script>
    export default {
        
    }
</script>

<style>

.card{
    background-color: rgb(255, 207, 118);
}

#container{
    margin: 0.2rem;
}

#description{
    padding: 0.1rem;
}

#image-styrkor{
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: -1rem;
}

h5{
    text-align: center;
}

</style>