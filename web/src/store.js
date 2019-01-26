import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export const store = new Vuex.Store({
  state: {
    access_token: ''
  },
  mutations: {
    authenticate(state, token) {
      state.access_token = token
    }
  }
})


Vue.http.interceptors.push((req, next) => {
  console.log('Call ', req);
  if (store.state.access_token) {
    req.headers.set('Authorization', 'Bearer ' + store.state.access_token);
  }
  next();
})
