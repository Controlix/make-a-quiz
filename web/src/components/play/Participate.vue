<template>
  <div>
    <h1>Play this awesome quiz</h1>
    <h2>{{quiz.name}}</h2>
  </div>
</template>

<script>
import Vue from 'vue'
import VueResource from 'vue-resource'

Vue.use(VueResource);

export default {
  name: 'Participate',
  data() {
    return {
      quiz: {}
    }
  },
  beforeRouteEnter(to, from, next) {
    Vue.http.get('http://localhost:5000/quiz/' + to.params['name']).then(
      (resp, err) => next(vm => vm.setData(resp, err))
    );
  },
  beforeRouteUpdate(to, from, next) {
    this.$http.get('http://localhost:5000/quiz/' + to.params['name']).then(
      resp => { this.quiz = resp.body },
      resp => { console.log('Something went wrong', resp) }
    );
  },
  methods: {
    setData(resp, err) {
      if (err) {
        console.log('Something went wrong', err);
      } else {
        this.quiz = resp.body;
        console.log(this.quiz);
      }
    }
  }
}
</script>

<style scoped>
</style>
