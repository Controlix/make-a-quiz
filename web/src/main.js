import Vue from 'vue'
import VueRouter from 'vue-router'

import App from './App.vue'
import CreateQuiz from './components/admin/Create'
import Participate from './components/play/Participate'


Vue.config.productionTip = false

Vue.use(VueRouter)

new Vue({
  router: new VueRouter({
    routes: [
      { path: '/create', component: CreateQuiz },
      { path: '/play', component: Participate }
    ]
  }),
  render: h => h(App),
}).$mount('#app')
