<template>
    <div class = "card-analyze" >

         <a href="#" v-scroll-to="{ element: '#container-side-bar-analyze', duration: 2000 }">

        <div id="description-analyze">
            <div id = container-analyze>
                <h3 id="analyze-text-card">Analyser dina styrkor & svagheter</h3>
                <div id="image-styrkor"> <img src="~/assets/images/styrkor.png" width=40% height=40% ></div>
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

.card-analyze{
    /* background-color: #284b63; */
    /* background-color: #4f6367; */
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

.card-analyze:hover{
   transform: scale(1.1); 
   box-shadow: 52px 52px 52px rgba(0, 0, 0, 0.2);
   transform: translateY(-10px);
   
   border-bottom: 5px solid rgb(226, 87, 69);
   transition: 0.3s;

}

#container-analyze{
    margin: 0.2rem;
}

#description-analyze{
    padding: 0.1rem;
}

#image-styrkor{
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: -1rem;
}

#analyze-text-card{
    text-align: center;
    padding:6px;
    font-family: 'Lato', sans-serif;
    color:rgb(0, 0, 0);
}

</style>