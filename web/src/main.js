import Vue from 'vue'
import VueRouter from 'vue-router'
import BootstrapVue from 'bootstrap-vue'
import Icon from 'vue-awesome/components/Icon'

import App from './App.vue'
import ListQuizes from './components/admin/List'
import CreateQuiz from './components/admin/Create'
import Participate from './components/play/Participate'

import {store} from './store'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'vue-awesome/icons'

Vue.config.productionTip = false

Vue.use(VueRouter)
Vue.component('v-icon', Icon)
Vue.use(BootstrapVue)

new Vue({
  router: new VueRouter({
    routes: [
      { path: '/', component: ListQuizes, name: 'home' },
      { path: '/create', component: CreateQuiz, name: 'new' },
      { path: '/play/:name', component: Participate, name: 'play' }
    ]
  }),
  store,
  render: h => h(App),
}).$mount('#app')
