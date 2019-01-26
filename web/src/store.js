import Vue from 'vue'
import Vuex from 'vuex'
import jwt from 'jsonwebtoken'

Vue.use(Vuex)

export const store = new Vuex.Store({
  state: {
    access_token: '',
    refresh_token: ''
  },
  mutations: {
    authenticate(state, tokens) {
      state.access_token = tokens.access_token;
      state.refresh_token = tokens.refresh_token;
    }
  }
})


Vue.http.interceptors.push((req, next) => {
  console.log('Call ', req);
  if (store.state.access_token) {
    req.headers.set('Authorization', 'Bearer ' + store.state.access_token);
    const decoded = jwt.decode(store.state.access_token);
    if (decoded && decoded.exp < new Date()/1000) {
      console.log('Access Token expired', decoded.exp);
      console.log(new Date(decoded.exp * 1000));
    }
  }
  next();
})
