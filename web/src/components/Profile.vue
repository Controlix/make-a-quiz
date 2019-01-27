<template>
  <div>
    <b-form @submit="do_login" inline v-if="!isLoggedIn">
      <label class="mr-sm-2" for="textInput">Username:</label>
      <b-form-input id="username"
                    class="mb-2 mr-sm-2 mb-sm-0"
                    type="text"
                    v-model="username"
                    required
                    placeholder="Enter your username">
      </b-form-input>
      <b-form-input id="password"
                    class="mb-2 mr-sm-2 mb-sm-0"
                    type="password"
                    v-model="password"
                    required
                    placeholder="Enter your password">
      </b-form-input>
      <b-button type="submit">
        Login
      </b-button>
    </b-form>
    <b-button v-else v-on:click="do_logout">
      Logout
    </b-button>
  </div>
</template>

<script>
import {mapMutations, mapGetters} from 'vuex'

export default {
  name: 'UserProfile',
  data() {
    return {
      username: "",
      password: ""
    }
  },
  computed: {
    ...mapGetters(['isLoggedIn'])
  },
  methods: {
    ...mapMutations(['authenticate', 'login', 'logout']),
    do_login() {
      this.$http.post('http://localhost:5000/login', { username: this.username, password: this.password }).then(
        resp => {
          this.login();
          this.authenticate(resp.body) },
        () => this.logout()
      );
    },
    do_logout() {
      this.$http.delete('http://localhost:5000/logout');
      this.logout();
    }
  }
}
</script>

<style>
</<style>s
