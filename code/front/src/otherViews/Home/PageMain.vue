<template>
    <div class="main-container">
            <!-- 顶部导航 -->
            <header class="block">
                <ul class="header-menu horizontal-list">
                    <li>
                        <a class="header-menu-tab" href="#1"><span class="icon entypo-cog "></span>Settings</a>
                    </li>
                    <li>
                        <a class="header-menu-tab" href="#2"><span class="icon fontawesome-user scnd-font-color"></span>Account</a>
                    </li>
                    <li>
                        <a class="header-menu-tab" href="#3"><span class="icon fontawesome-envelope scnd-font-color"></span>Messages</a>
                        <a class="header-menu-number" href="#4">5</a>
                    </li>
                    <li>
                        <a class="header-menu-tab" href="#5"><span class="icon fontawesome-star-empty scnd-font-color"></span>Favorites</a>
                    </li>
                </ul>
                <div class="profile-menu">
                    <p>Me <a href="#26"><span class="entypo-down-open scnd-font-color"></span></a></p>
                    <div class="profile-picture small-profile-picture">
                        <img width="40px" alt="Anne Hathaway picture" src="http://upload.wikimedia.org/wikipedia/commons/e/e1/Anne_Hathaway_Face.jpg">
                    </div>
                </div>
            </header>
        </div> <!-- end main-container -->
</template>

<script>
export default {
  name:'PageMain'
}
</script>

<style lang="scss" scope>
/************************************ FONTS ************************************/
@import url(https://fonts.googleapis.com/css?family=Ubuntu:400,700);
@import url(https://weloveiconfonts.com/api/?family=entypo|fontawesome|zocial);
/* entypo */
[class*="entypo-"]:before {
  font-family: "entypo", sans-serif;
}
/* fontawesome */
[class*="fontawesome-"]:before {
  font-family: "FontAwesome", sans-serif;
}
/* zocial */
[class*="zocial-"]:before {
  font-family: "zocial", sans-serif;
}
/************************************* END FONTS *************************************/
main-container {

  width: 100%;
  height: 100%;
}

ul {
  list-style-type: none;
  margin: 0;
  padding-left: 0;
}

h1 {
  font-size: 23px;
}

h2 {
  font-size: 17px;
}

p {
  font-size: 15px;
}

a {
  text-decoration: none;
  font-size: 15px;
}
a:hover {
  text-decoration: underline;
}

.horizontal-list {
  margin: 0;
  padding: 0;
  list-style-type: none;
}
.horizontal-list li {
  float: left;
}
.icon {
  font-size: 25px;
}
.button {
  display: block;
  width: 175px;
  line-height: 50px;
  font-size: 16px;
  font-weight: 700;
  text-align: center;
  margin: 0 auto;
  border-radius: 5px;
  -webkit-transition: background 0.3s;
  transition: background 0.3s;
}
.button:hover {
  text-decoration: none;
}
.profile-picture {
  border-radius: 100%;
  overflow: hidden;
  -webkit-box-sizing: content-box;
  -moz-box-sizing: content-box;
  box-sizing: content-box;
}
// 用户头像
.small-profile-picture {
  border: 2px solid #50597b;
  width: 40px;
  height: 40px;
}

/** MAIN CONTAINER **/

.main-container {
  font-family: "Ubuntu", sans-serif;
  width: 100%;
  height: 100%;
  margin: 0em auto;
}
/*********************************************** HEADER ***********************************************/
header {
  height: 80px;
}
.header-menu {
  font-size: 17px;
  line-height: 80px;
}
.header-menu li {
  position: relative;
  -webkit-transform: translateZ(0); /** To avoid a flash when hover messages **/
}
.header-menu-tab {
  padding: 0 27px;
  display: block;
  line-height: 74px;
  font-size: 17px;
  -webkit-transition: background 0.3s;
  transition: background 0.3s;
  color: black;
}
.header-menu-tab:hover {
  background: #a0a0a0;
  border-bottom: 4px solid #11a8ab;
  text-decoration: none;
}
.header-menu-tab .icon {
  padding-right: 15px;
}
.header-menu-number {
  position: absolute;
  line-height: 22px;
  padding: 0 6px;
  font-weight: 700;
  background: #e64c65;
  border-radius: 100%;
  color: white;
  top: 15px;
  right: 2px;
  -webkit-transition: all 0.3s linear;
  transition: all 0.3s linear;
}
.header-menu li:hover .header-menu-number {
  text-decoration: none;
  -webkit-transform: rotate(360deg);
  transform: rotate(360deg);
}
.profile-menu {
  float: right;
  height: 80px;
  padding-right: 20px;
}
.profile-menu p {
  font-size: 17px;
  display: inline-block;
  line-height: 76px;
  margin: 0;
  padding-right: 10px;
}
.profile-menu a {
  padding-left: 5px;
}
.profile-menu a:hover {
  text-decoration: none;
}
.small-profile-picture {
  display: inline-block;
  vertical-align: middle;
}
/** CONTAINERS **/
.container {
  float: left;
  width: 300px;
}
.block {
  margin-bottom: 25px;
  background: #ffffff;
  border-radius: 5px;
}
</style>