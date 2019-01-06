<template>
  <div id="app">
    <img alt="Quiz" src="./assets/Quiz.png">
    <h1>Welcome to my quiz app!</h1>
    <p>
      <router-link to='/create'>Create a new quiz</router-link>
      <br />
      <router-link to='/play'>Play a quiz</router-link>
    </p>
    <router-view></router-view>
  </div>
</template>

<script>export default {
  name: 'app'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
