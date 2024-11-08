<template>
        <nav class="food-nav">
        <ul>
          <li>
            <a href="#">长沙</a>
          </li>
          <li>
            <a href="#">湘潭</a>
          </li>
          <li>
            <a href="#">株洲</a>
          </li>
          <li>
            <a href="#">益阳</a>
          </li>
          <li>
            <a href="#">萍乡</a>
          </li>
        </ul>
      </nav>
</template>

<script>
export default {
  name: "CityNav",
  data: {
    // 假设这是从后端获取的数据
    navItems: [
      { text: "长沙", href: "#item1" },
      { text: "湘潭", href: "#item2" },
      { text: "Nav Item 3", href: "#item3" },
      { text: "Nav Item 4", href: "#item4" },
      { text: "Nav Item 5", href: "#item5" },
    ],
  },
};
</script>

<style lang="scss" scope>
/* All */
.food-nav {
  margin-bottom: 5px;
  width: auto;
}
.food-nav ul {
  *zoom: 1;
  list-style: none;
  margin: 0;
  padding: 0;
  background: #333;
  display: inline-block;
}
.food-nav ul:before,
.food-nav ul:after {
  content: "";
  display: table;
}
.food-nav ul:after {
  clear: both;
}
.food-nav ul > li {
  float: left;
  position: relative;
}
.food-nav a {
  display: block;
  padding: 10px 20px;
  line-height: 1.2em;
  color: #fff;
  border-left: 1px solid #595959;
}
.food-nav a:hover {
  text-decoration: none;
  background: #595959;
}
</style>