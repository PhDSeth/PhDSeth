<template>
    <div class = "card" >

        <div id="description">
            <div id = container>
                <h5>Använd vår unika sökfunktion</h5>
                <div id="image-styrkor"> <img src="~/assets/images/sök.png" width=40% height=40% ></div>
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
    width: 8rem;
    height: 8rem;
}

#container{
    margin: 0.2rem;
}

#description{
    padding: 0.1rem;
}

#image-search{
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: -1rem;
}

h5{
    text-align: center;
}

</style>