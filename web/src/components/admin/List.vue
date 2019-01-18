<template>
  <div>
    <h1>All Your Quizes</h1>
    <b-table :items="quizes">
      <template slot="questions" slot-scope="cell">
        {{cell.item.questions.length}}
      </template>
    </b-table>
  </div>
</template>

<script>
import Vue from 'vue'
import VueResource from 'vue-resource'

Vue.use(VueResource);

export default {
  name: 'ListQuizes',
  data() {
    return {
      quizes: []
    }
  },
  created() {
    this.loadQuizes();
  },
  methods: {
    loadQuizes() {
      this.$http.get('http://localhost:5000/quiz').then(
        resp => { this.quizes = resp.body },
        resp => { console.log('Something went wrong', resp) }
      );
    }
  }
}

</script>

<style scoped>
</style>
