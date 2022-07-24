<template>
    <div class = "price">
        <h1 id="title-price">Lås upp alla funktioner för 69 kr ( = 1,5 kaffe-latte) </h1>

        <br>
        <br>
        <p id = "text-price">
            Varför är inte tjänsten gratis undrar du. Bra fråga tycker vi! 
            Att utveckla och underhålla en webbsida är inte gratis. Därför behöver vi ta ut en avgift för att vi ska kunna fortsätta utveckla våra tjänster. Vi har försökt att hålla avgiften så låg som möjligt, samtidigt som vi inte vill tumma på .
            Vi vill helt enkelt att så många som möjligt ska få ut så mycket som möjligt av oss.
            <br>
            <br>
            Vi skäner dessutom 5% av våra intäkter till BLBLA. Bra va? 
            
        </p>



    </div>
</template>

<script>
    export default {
        
    }
</script>

<style>

.price{
    position:absolute;
    /* background-color: black; */
    height:10rem;
    display:flex;
    flex-direction: column;
    align-items: center;
    margin-top:1rem;
    bottom:-95rem;
    width: 90vw;
    padding:3rem;
    margin-left:3rem;
}


#title-price{
    color:rgb(0, 0, 0);
    
}

#text-price{
    font-size:1.3rem;
    text-align:center;
}

</style>