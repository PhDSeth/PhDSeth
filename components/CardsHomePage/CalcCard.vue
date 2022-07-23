<template>
    <div class = "card-calc" >

          <a href="#" v-scroll-to="{ element: '#container-side-bar-calc', duration: 2000 }">
        <div id="description-calc">
            <div id = contcalcner-calc>
                <h3 id ="calc-text-card">Ta reda på dina betyg & behörighet</h3>
                <div id="image-styrkor"> <img src="~/assets/images/räkna.png" width=40% height=40% ></div>
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

.card-calc{
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

.card-calc:hover{
   transform: scale(1.1); 
   box-shadow: 52px 52px 52px rgba(0, 0, 0, 0.2);
   transform: translateY(-10px)

}

#contcalcner-calc{
    margin: 0.2rem;
}

#description-calc{
    padding: 0.1rem;
}

#image-styrkor{
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: -1rem;
}

#calc-text-card{
    text-align: center;
    padding:6px;
    font-family: 'Lato', sans-serif;
    color:rgb(0, 0, 0);
}

</style>