<template>
  <div class="food">
    <div class="food-content">

    <CascadeSelect
      v-model="selectedCity"
      :options="countries"
      optionLabel="cname"
      optionGroupLabel="name"
      :optionGroupChildren="['states', 'cities']"
      style="minwidth: 14rem"
    ></CascadeSelect>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import CascadeSelect from "primevue/cascadeselect";
export default {
  name: "food",
  components: {
    CascadeSelect,
  },
  data() {
    return {
      data: "",
      selectedCity: null,
      countries: [
        {
          name: "Australia",
          code: "AU",
          states: [
            {
              name: "New South Wales",
              cities: [
                { cname: "Sydney", code: "A-SY" },
                { cname: "Newcastle", code: "A-NE" },
                { cname: "Wollongong", code: "A-WO" },
              ],
            },
            {
              name: "Queensland",
              cities: [
                { cname: "Brisbane", code: "A-BR" },
                { cname: "Townsville", code: "A-TO" },
              ],
            },
          ],
        },
        {
          name: "Canada",
          code: "CA",
          states: [
            {
              name: "Quebec",
              cities: [
                { cname: "Montreal", code: "C-MO" },
                { cname: "Quebec City", code: "C-QU" },
              ],
            },
            {
              name: "Ontario",
              cities: [
                { cname: "Ottawa", code: "C-OT" },
                { cname: "Toronto", code: "C-TO" },
              ],
            },
          ],
        },
        {
          name: "United States",
          code: "US",
          states: [
            {
              name: "California",
              cities: [
                { cname: "Los Angeles", code: "US-LA" },
                { cname: "San Diego", code: "US-SD" },
                { cname: "San Francisco", code: "US-SF" },
              ],
            },
            {
              name: "Florida",
              cities: [
                { cname: "Jacksonville", code: "US-JA" },
                { cname: "Miami", code: "US-MI" },
                { cname: "Tampa", code: "US-TA" },
                { cname: "Orlando", code: "US-OR" },
              ],
            },
            {
              name: "Texas",
              cities: [
                { cname: "Austin", code: "US-AU" },
                { cname: "Dallas", code: "US-DA" },
                { cname: "Houston", code: "US-HO" },
              ],
            },
          ],
        },
      ],
    };
  },
  created() {
    this.show();
  },
  methods: {
    async show() {
      try {
        const response = await axios.get(
          "http://localhost:8081/ManagerHome/CityData/food"
        );
        this.data = response.data[0];
        console.log(this.data)
      } catch (error) {
        console.error("Error loading data:", error);
      } finally {
      }
    },
  },
};
</script>

<style lang="scss" scope>
.food {
  height: 1280px;
  width: 1280px;
  background-color: rgb(255, 255, 255);

}
.food-content{
   position: absolute;
   margin-top:20px ;
   margin-left: 20px;

}
</style>