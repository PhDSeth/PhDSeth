<template>
    <div class = "Map">

        <div id="map-wrap" style="height: 80vh">
        <client-only>
        <l-map :zoom=13 :center="[55.9464418,8.1277591]">
            <l-tile-layer url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"></l-tile-layer>
            <l-marker v-for = "cord in coordinates" :key="cord.id" :lat-lng="cord.cord"><l-popup :content="cord.id"/></l-marker>
        </l-map>
        </client-only>
        </div>
    </div>
</template>

<script>

    export default {
        
        data(){

            return {
                coordinates: [
                    {
                    "city" : "Umeå",
                    "cord": [63.825848, 20.263035], 
                    "id":"1"
                    },
                    {
                    "city" : "Göteborg",
                    "cord": [57.708870, 11.974560], 
                    "id":"2"
                    },
                    {
                    "city" : "Stockholm",
                    "cord": [59.334591, 18.063240], 
                    "id": "3"
                    },
                   

                ],

                hejObjekt: ""
            }
        },

        methods: {

            hej(){
                this.hejObjekt = "HEj"
                
            }

        }


    }
</script>

<style >
.Map{
    height: 10rem;
    width: 20rem;
}

</style>