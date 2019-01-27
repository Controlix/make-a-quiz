<template>
  <div>
    <b-nav-item-dropdown right no-caret>
      <template slot="button-content">
        <v-icon name="regular/user-circle" scale="1.5"/>
      </template>
      <b-dropdown-item v-b-modal.login-form v-if="!isLoggedIn">Login</b-dropdown-item>
      <b-dropdown-item v-on:click="do_logout" v-else>Logoff</b-dropdown-item>
    </b-nav-item-dropdown>
    <b-modal id="login-form" title="Login" v-on:ok="do_login" v-on:cancel="clear_login_form">
      <label class="mr-sm-2" for="textInput">Username:</label>
      <b-form-input id="username"
                    class="mb-2 mr-sm-2 mb-sm-0"
                    type="text"
                    v-model="username"
                    required
                    placeholder="Enter your username">
      </b-form-input>
      <label class="mr-sm-2" for="textInput">Password:</label>
      <b-form-input id="password"
                    class="mb-2 mr-sm-2 mb-sm-0"
                    type="password"
                    v-model="password"
                    required
                    placeholder="Enter your password">
      </b-form-input>
    </b-modal>
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
      const username = this.username;
      const password = this.password;
      this.clear_login_form();
      this.$http.post('http://localhost:5000/login', { username: username, password: password }).then(
        resp => {
          this.login();
          this.authenticate(resp.body) },
        () => this.logout()
      );
    },
    do_logout() {
      this.$http.delete('http://localhost:5000/logout');
      this.logout();
    },
    clear_login_form() {
      this.username = '';
      this.password = '';
    }
  }
}
</script>

<style>
</<style>s
