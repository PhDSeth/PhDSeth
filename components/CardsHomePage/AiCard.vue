<template>
    <div class = "card-ai" >
         <a href="#" v-scroll-to="{ element: '#container-side-bar-ai', duration: 2000 }">
        <div id="description-ai">
            <div id = container-ai>
                <h3 id="ai-text-card">Ta reda på dina chanser att komma in</h3>
                <div id="image-styrkor"> <img src="~/assets/images/ai.png" width=40% height=40% ></div>
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

.card-ai{
    /* background-color: #2f6690; */
    /* background-color: #284b63; */
    /* background-color: #4f6367; */
    background-color: #f3f7fe;
    width:15vw;
    height: 22vh;
    margin-top:-1rem;
    box-shadow: 20px 20px 20px rgba(0, 0, 0, 0.2);
    border: solid;
    border-color: #342773;
    border-radius: 0.4rem;
    border-width: 1px;
}

.card-ai:hover{
   transform: scale(1.1); 
   box-shadow: 52px 52px 52px rgba(0, 0, 0, 0.2);
   transform: translateY(-10px)

}

#container-ai{
    margin: 0.2rem;
}

#description-ai{
    padding: 0.1rem;
}

#image-styrkor{
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: -1rem;
}

#ai-text-card{
    text-align: center;
    padding:6px;
    font-family: 'Lato', sans-serif;
    color:rgb(0, 0, 0);
}

</style>