<template>
    <div class = "card-search" >
        <a href="#" v-scroll-to="{ element: '#container-side-bar-search', duration: 2000 }">

            <div id="description-search">
                <div id = container-search>
                    <h3 id="search-text-card">Hitta drömutbildningen du inte visste fanns</h3>
                    <div id="image-styrkor"> <img src="~/assets/images/sök.png" width=40% height=40% ></div>
                </div>
            
            </div>
        </a>

        

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
    box-shadow: 20px 20px 20px rgba(0, 0, 0, 0.2);
    border: solid;
    border-color: white;
    border-radius: 0.4rem;
    /* border-width: 2px;
    border-color:rgb(154, 30, 123); */

    border-bottom: 2px solid rgb(226, 87, 69);
}

.card-search:hover{
   transform: scale(1.1); 
   box-shadow: 52px 52px 52px rgba(0, 0, 0, 0.2);
   transform: translateY(-10px);
      border-bottom: 5px solid rgb(226, 87, 69);
   transition: 0.3s;

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