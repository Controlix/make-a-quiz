<template>
  <div id="app">
    <img alt="Quiz" src="./assets/Quiz.png">
    <CreateQuiz></CreateQuiz>
    <Participate></Participate>
  </div>
</template>

<script>
import CreateQuiz from './components/admin/Create.vue'
import Participate from './components/play/Participate.vue'

export default {
  name: 'app',
  components: {
    CreateQuiz, Participate
  }
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
