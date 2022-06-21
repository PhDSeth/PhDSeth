<template>
    <div class = "card" >

        <div id="description">
            <div id = container>
                <h3 id ="goal">Sätt upp & följ dina mål</h3>
                <div id="image-styrkor"> <img src="~/assets/images/mål.png" width=40% height=40% ></div>
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
    padding: 1 rem;
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

#goal{
    text-align: center;
}

</style>