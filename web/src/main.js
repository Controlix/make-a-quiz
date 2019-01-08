import Vue from 'vue'
import VueRouter from 'vue-router'

import App from './App.vue'
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
      { path: '/create', component: CreateQuiz },
      { path: '/play', component: Participate }
    ]
  }),
  render: h => h(App),
}).$mount('#app')
