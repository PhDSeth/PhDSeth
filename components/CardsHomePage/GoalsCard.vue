<template>
    <div class = "card-goal" >

        <div id="description-goal">
            <div id = container-goal>
                <h3 id ="goal-text-card">Sätt upp & följ dina mål</h3>
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

.card-goal{
    /* background-color: #2f6690; */
    /* background-color: #284b63; */
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

.card-goal:hover{
   transform: scale(1.1); 
   box-shadow: 52px 52px 52px rgba(0, 0, 0, 0.2);
   transform: translateY(-10px)

}

#container-goal{
    margin: 0.2rem;
}

#description-goal{
    padding: 0.1rem;
}

#image-styrkor{
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: -1rem;
}

#goal-text-card{
    text-align: center;
    padding:6px;
    font-family: 'Lato', sans-serif;
    color:rgb(0, 0, 0);
}

</style>