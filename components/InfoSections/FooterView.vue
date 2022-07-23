<template>
    <div class ="footer">
      
            <div class = "left-footer">
                <h3 id="title-left-footer">Om oss</h3>
                <br>
                <p id="p-left-footer">Vi som står bakom Studielabbet har tillsammans över 10 års erfarenhet av studier på universitetsnivå. 
                    Utöver det har vi även erfarenhet av utbildningsmässor och undervisning på universitetsnivå. 
                    Vi vet vad som efterfrågas av blivande studenter.
                    Därför har vi utvecklat denna tjänst som är tänkt att göra livet lite enklare för dig som blivande student.
                    <br>
                    <br>
                    Våra funktioner bygger på data som inhämtats från myndigheter samt universitet och högskolor i Sverige. De funktioner som bygger på artificiell intelligens (AI) är testade och granskade.  
                </p>

            </div>

            <div class = "right-footer">
                <h3  id="title-right-footer">Kontakt</h3>
                <p>Vi förstår om du har frågor! Tveka inte att höra av dig om du undrar något. 
                    Maila oss på: <a href="/">info@studielabbet.se</a> eller skriv till oss på Instagram eller Facebook.
                </p>

                <br>
                <br>
                 <h3  id="title-right-footer">Följ oss!</h3>
                 <div id="icons">
                    <font-awesome-icon id="icon-check-analyze" fa-6x :icon="['fab', 'instagram']" />
                    <font-awesome-icon id="icon-check-analyze" fa-6x :icon="['fab', 'facebook']" />
                    
                 </div>

            </div>



    </div>
</template>

<script>
    export default {
        
    }
</script>

<style lang="scss" scoped>

#icons{
    text-align:center;
    margin-top:1rem;
    font-size:2rem;
}
.footer{
    display:flex;
    flex-direction:row;
    background-image: linear-gradient(to right, #8dacf4, #602cca);
    width: 100vw;
    position:absolute;
    z-index:100;
    height:20rem;
    bottom:-120rem;
    margin-left:-1rem;
    color:white;
}

.left-footer{
    display:flex;
    flex-direction:column;
    justify-content: center;
    width: 50%;
    padding: 3rem;
    margin-top:-10px;
    text-align: center;
}

#title-left-footer{
    text-align: center;
}
.right-footer{
    display:flex;
    flex-direction:column;
    justify-content: center;
    width: 50%;
    padding: 3rem;
    margin-top:-10px;
}

#title-right-footer{
    text-align: center;
}


</style>