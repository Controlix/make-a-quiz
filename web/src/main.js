import Vue from 'vue'
import VueRouter from 'vue-router'

import App from './App.vue'
import ListQuizes from './components/admin/List'
import CreateQuiz from './components/admin/Create'
import Participate from './components/play/Participate'

import 'vue-awesome/icons'
import Icon from 'vue-awesome/components/Icon'

Vue.config.productionTip = false

Vue.use(VueRouter)
Vue.component('v-icon', Icon)

new Vue({
  router: new VueRouter({
    routes: [
      { path: '/', component: ListQuizes, name: 'home' },
      { path: '/create', component: CreateQuiz, name: 'new' },
      { path: '/play', component: Participate, name: 'play' }
    ]
  }),
  render: h => h(App),
}).$mount('#app')
