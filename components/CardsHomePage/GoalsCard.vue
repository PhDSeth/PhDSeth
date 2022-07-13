<template>
    <div class = "card-goal" >

        <div id="description-goal">
            <div id = container-goal>
                <h3 id ="goal-goal">Sätt upp & följ dina mål</h3>
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
    background-color: #acb4b5;
    width:15vw;
    height: 22vh;
    margin-top:-1rem;
    border-radius: 1.4rem;
    border-style: solid;
    border-color: rgb(74, 86, 85);
}

.card-goal:hover{
   transform: scale(1.1); 
   box-shadow: 52px 52px 52px rgba(0, 0, 0, 0.2);

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

h3{
    text-align: center;
    padding:6px;
    font-family: 'Lato', sans-serif;
    color:rgb(255, 255, 255);
}

</style>