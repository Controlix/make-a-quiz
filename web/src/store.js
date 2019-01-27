import Vue from 'vue'
import Vuex from 'vuex'
import jwt from 'jsonwebtoken'
import VuexPersistence from 'vuex-persist'

Vue.use(Vuex)

const vuexLocal = new VuexPersistence({
  key: 'make_a_quiz',
  storage: window.localStorage
})

export const store = new Vuex.Store({
  state: {
    access_token: '',
    refresh_token: ''
  },
  getters: {
    access_token: state => state.access_token,
    refresh_token: state => state.refresh_token
  },
  mutations: {
    authenticate(state, tokens) {
      state.access_token = tokens.access_token;
      state.refresh_token = tokens.refresh_token;
    }
  },
  plugins: [vuexLocal.plugin]
})


Vue.http.interceptors.push((req, next) => {
  console.log('Call ', req);
  if (store.state.access_token) {
    req.headers.set('Authorization', 'Bearer ' + store.state.access_token);
  }
  next((resp, err) => {
    if (resp.status === 401 && resp.body.msg === 'Token has expired') {
      console.log('Must refresh access token');
    }
  })
})
