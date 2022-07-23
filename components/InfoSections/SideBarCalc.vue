<template>
    <div id = "container-side-bar-calc">
        <div class="text-analyze-card-calc">
            <h1 id = "analyze-title-calc">Ta reda på dina betyg & behörighet</h1>
            <p id="analyze-text-calc">
            Vi har som ambition att göra livet enklare för dig som planerar att söka till universitet och högskolor i Sverige. Därför har vi utvecklat en rad olika smarta funktioner åt dig.
            Nu kan du för första gången räkna ut ditt betygssnitt helt automatiskt. Du behöver bara kopiera och klistra in dina betyg. Eller så fotar du dina betyg, och vi löser in dessa åt dig. Du kan också exportera betyget som en Excel-fil om du vill.

            <br>
            <br>
            Funktionen inkluderar:
            <ul>
                <div class="list-items-calc">
                <li>Automatisk uträkning av ditt betygssnitt</li>
                <li>Automatisk uträkning av vilka behörighetsgrupper du tillhör </li>
                </div>
            </ul>
 
            
            </p>
        </div>

        <div class = "img-analyze-card-calc">
            <img src="~/assets/images/grades.png" width=90% height=100% >
        </div>


    </div>
</template>

<script>
import VScrollin from "vue-scrollin";

    export default {
     
    }
</script>

<style>

.img-analyze-card-calc{
    margin-top: 2rem;
}

#container-side-bar-calc{
    margin-top:2rem;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    position:absolute;
    /* margin-top:110vh; */
    /* margin-left:-2rem; */
    padding: 2rem;
    /* background-color: #f4f9e9; */
    margin-top:275px;
    width: 90vw;
    margin-left:60px;
    background-image: linear-gradient(to right, #f1f5fe, #d9d7e2);
    /* border: solid; */
    /* border-color: #4a4d84; */
    border-radius: 0.4rem;


}

/* @keyframes slide-up {
  from {
    opacity: 0.2;
    transform: translateY(600px);

  }
  to{
    opacity:1;
    transform: translateY(20px);
  }
} */


a{
    text-decoration:none;
}

.text-analyze-card-calc{
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    width:60%;
    flex-wrap: wrap;
    padding: 2rem;
    animation: slide-up 3s;
    
}

#analyze-text-calc{
    font-size: 1.3rem;
}

#analyze-title-calc{
    margin-bottom: 1.6rem;
}

.list-items-calc{
    margin-left:50px;
}

:root {
    --bg: #fdfdfd;
    --highlight1: #ED4264;
    --highlight2: #FFEDBC;
    --color: #1a1e24;
    --font-number: Montserrat, Roboto, Helvetica, Arial, sans-serif;
    --font-head: "Space Mono", Consolas, Menlo, Monaco, "Courier New", monospace;
    --font: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
}



</style>