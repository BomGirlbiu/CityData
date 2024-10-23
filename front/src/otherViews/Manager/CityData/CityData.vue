<template>
  <div class="city-data">
    城市信息管理
    <TabMenu :model="items" />
    <router-view />
  </div>
</template>

<script>
import TabMenu from "primevue/tabmenu";
export default {
  name: "CityData",
  components: {
    TabMenu,
  },
  data() {
    return {
      items: [
        { label: "美食", icon: "pi pi-fw pi-home", to: "food" },
        {
          label: "旅游",
          icon: "pi pi-fw pi-calendar",
          to: "travel",
        },
        { label: "新闻", icon: "pi pi-fw pi-pencil", to: "news" },      ],
    };
  },
};
</script>

<style>
</style>