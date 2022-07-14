<template>
    <div class = "card-search" >

        <div id="description-search">
            <div id = container-search>
                <h3 id="search-text-card">Använd vår unika sökfunktion</h3>
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

.card-search{
    /* background-color: #2f6690; */
    /* background-color: #284b63; */
     background-color: #f3f7fe;
    width:15vw;
    height: 22vh;
    margin-top:-1rem;
}

.card-search:hover{
   transform: scale(1.1); 
   box-shadow: 52px 52px 52px rgba(0, 0, 0, 0.2);
   transform: translateY(-10px)

}

#container-search{
    margin: 0.2rem;
}

#description-search{
    padding: 0.1rem;
}

#image-styrkor{
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: -1rem;
}

#search-text-card{
    text-align: center;
    padding:6px;
    font-family: 'Lato', sans-serif;
    color:rgb(0, 0, 0);
}

</style>