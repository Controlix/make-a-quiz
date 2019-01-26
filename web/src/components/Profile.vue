<template>
  <div>
    <b-form @submit="login" inline>
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
      <b-button type="submit" variant="success">
      </b-button>
    </b-form>
  </div>
</template>

<script>
import {mapMutations} from 'vuex'

export default {
  name: 'UserProfile',
  data() {
    return {
      username: "",
      password: ""
    }
  },
  methods: {
    ...mapMutations(['authenticate']),
    login() {
      console.log("Login with " + this.username + " and " + this.password);
      this.$http.post('http://localhost:5000/login', { username: this.username, password: this.password }).then(
        resp => { this.authenticate(resp.body['access_token']) },
        resp => { console.log('Something went wront', resp) }
      );
    }
  }
}
</script>

<style>
</<style>s
