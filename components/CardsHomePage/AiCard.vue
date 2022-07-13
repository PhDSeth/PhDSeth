<template>
    <div class = "card-ai" >
         
        <div id="description-ai">
            <div id = container-ai>
                <h3>Ta reda på dina betyg & behörighet</h3>
                <div id="image-styrkor"> <img src="~/assets/images/ai.png" width=40% height=40% ></div>
            </div>
           
        </div>

        

    </div>
</template>

<script>
    export default {
        
    }
</script>

<style>

.card-ai{
    background-color: #2f6690;
    width:15vw;
    height: 22vh;
    margin-top:-1rem;
    border-radius: 1.4rem;
    border-style: solid;
    border-color: 344966;
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

h3{
    text-align: center;
    padding:6px;
    font-family: 'Lato', sans-serif;
    color:rgb(255, 255, 255);
}

</style>