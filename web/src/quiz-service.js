import Vue from 'vue'
import VueResource from 'vue-resource'

Vue.use(VueResource);

export default {
  allQuizes() {
    return Vue.http.get('http://localhost:5000/quiz').then(
      resp => { return resp.body },
      error => { return [] }
    )
  },
  quiz(id) {
    return Vue.http.get('http://localhost:5000/quiz/' + id).then(
      resp => { return resp.body },
      error => { return {} }
    )
  }
}
