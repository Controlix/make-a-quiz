<template>
  <div id="app">
    <img alt="Quiz" src="./assets/Quiz.png">
    <h1>Welcome to my quiz app!</h1>
    <b-navbar toggleable="md" type="dark" variant="success">
      <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>
      <b-navbar-brand to="/">Make a Quiz</b-navbar-brand>
      <b-collapse is-nav id="nav_collapse">
        <b-navbar-nav v-if="isLoggedIn">
          <b-nav-item to='/create'>Create a new quiz</b-nav-item>
          <b-nav-item to='/play'>Play a quiz</b-nav-item>
        </b-navbar-nav>
        <b-navbar-nav right class="ml-auto">
          <user-profile></user-profile>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <router-view></router-view>
  </div>
</template>

<script>
import UserProfile from './components/Profile'
import {mapGetters} from 'vuex'

export default {
  name: 'app',
  components: { UserProfile },
  computed: {
    ...mapGetters(['isLoggedIn'])
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
