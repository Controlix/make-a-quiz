<template>
  <div>
    <h1>Play this awesome quiz</h1>
    <h2>{{name}}</h2>
    <b-table :items="questions">

    </b-table>
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
      name: '',
      questions: []
    }
  },
  beforeRouteEnter(to, from, next) {
    const name = to.params['name'];
    Vue.http.get('http://localhost:5000/quiz/' + name + '/questions').then(
      (resp, err) => next(vm => vm.setData(name, resp, err))
    );
  },
  beforeRouteUpdate(to, from, next) {
    this.$http.get('http://localhost:5000/quiz/' + to.params['name']).then(
      resp => { this.quiz = resp.body },
      resp => { console.log('Something went wrong', resp) }
    );
  },
  methods: {
    setData(name, resp, err) {
      this.name = name;
      if (err) {
        console.log('Something went wrong', err);
      } else {
        console.log(resp);
        this.questions = resp.body;
        console.log(this.questions);
      }
    }
  }
}
</script>

<style scoped>
</style>
