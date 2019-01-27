import Vue from 'vue'
import Vuex from 'vuex'
import VuexPersistence from 'vuex-persist'

Vue.use(Vuex)

const vuexLocal = new VuexPersistence({
  key: 'make_a_quiz',
  storage: window.localStorage
})

export const store = new Vuex.Store({
  state: {
    access_token: '',
    refresh_token: '',
    status: 'UNKNOWN'
  },
  getters: {
    isLoggedIn: state => state.status === 'LOGGED_IN'
  },
  mutations: {
    login(state, tokens) {
      state.access_token = tokens.access_token;
      state.refresh_token = tokens.refresh_token;
      state.status = 'LOGGED_IN';
    },
    refresh(state, tokens) {
      state.access_token = tokens.access_token;
      state.status = 'LOGGED_IN';
    },
    start_refresh(state) {
      state.status = 'REFRESHING';
    },
    logout(state) {
      state.access_token = '';
      state.refresh_token = '';
      state.status = 'UNKNOWN';
    }
  },
  plugins: [vuexLocal.plugin]
})


Vue.http.interceptors.push((req, next) => {
  if (store.state.status === 'LOGGED_IN') {
    req.headers.set('Authorization', 'Bearer ' + store.state.access_token);
  }
  if (store.state.status === 'REFRESHING') {
    req.headers.set('Authorization', 'Bearer ' + store.state.refresh_token);
  }
  next((resp) => {
    if (resp.status === 401) {
      if (store.state.status === 'LOGGED_IN' && resp.body.msg === 'Token has expired') {
        store.commit('start_refresh');
        return Promise.resolve(
          Vue.http.get('http://localhost:5000/refresh').then(
            resp => { store.commit('refresh', resp.body) }
          ).then(() => Vue.http(req)));
      } else {
        store.commit('logout');
      }
    }
  })
})
