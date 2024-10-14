<template>
  <table class="rank-table">
    <thead class="rank-thead">
        <tr>
            <th>Rank</th>
            <th>Item Name</th>
            <th>Status</th>
        </tr>
    </thead>

  <tbody>
        <tr>
            <td>
              <div class="rank">1</div>
              <div class="draganddrop"></div>
            </td>
            <td class="name">
              Item Name
            </td>
            <td class="status in-progress">
              in-progress
            </td>
        </tr>
        <tr>
            <td>
              <div class="rank">2</div>
              <div class="draganddrop"></div>
            </td>
            <td class="name">
              Item Name
            </td>
            <td class="status in-progress">
              in-progress
            </td>
        </tr>
        <tr>
            <td>
              <div class="rank">3</div>
              <div class="draganddrop"></div>
            </td>
            <td class="name">
              Item Name
            </td>
            <td class="status open">
              open
            </td>
        </tr>
        <tr>
            <td>
              <div class="rank">1</div>
              <div class="draganddrop"></div>
            </td>
            <td class="name">
              Item Name
            </td>
            <td class="status overdue">
              overdue
            </td>
        </tr>
    </tbody>
</table>
</template>

<script>
export default {
    name:"RankTable"
}
</script>

<style lang="scss" scope>
@import "http://www.elyseholladay.com/p360/fonts/fonts.css";
body {
  font-family: "ProximaNovaRegular", Arial, sans-serif;
  font-size: 100%;
}

.rank-table {
  border-collapse: collapse;
  border-spacing: 0;
  width: 600px;
}

.rank-thead {
  background: #ccc;
  line-height: 3.5em;
  text-align: left;
  text-transform: uppercase;
  font-size: 0.75em;
  color: #262626;
}
.rank-thead th {
  padding-left: 2em;
  font-family: "ProximaNovaBold";
}

tr {
  line-height: 3em;
  border-bottom: 1px solid #ccc;
}
tr td {
  padding-left: 1.5em;
}

.rank {
  display: inline-block;
  vertical-align: 3px;
  font-size: 0.85em;
  font-family: "ProximaNovaBold";
  margin-right: 2em;
}

.status {
  font-family: "ProximaNovaBold";
  font-size: 0.75em;
  text-transform: uppercase;
}
.status.in-progress {
  color: #9eca69;
}
.status.open {
  color: #f5c149;
}
.status.overdue {
  color: red;
}

.draganddrop {
  display: inline-block;
  border-top: 2px solid #ccc;
  width: 25px;
  padding-top: 2px;
  cursor: -webkit-grab;
  cursor: -moz-grab;
}

.draganddrop:before,
.draganddrop:after {
  display: block;
  content: "";
  border-top: 2px solid #ccc;
  padding-top: 2px;
}

.draganddrop:hover,
.draganddrop:hover:before,
.draganddrop:hover:after {
  border-color: #57b5d6;
}

.draganddrop:active,
.draganddrop:active:before,
.draganddrop:active:after {
  cursor: -webkit-grabbing;
  cursor: -moz-grabbing;
}
</style>