<template>
  <div>
    <h1>All Your Quizes</h1>
    <b-table :items="quizes" :fields="fields">
      <template slot="questions" slot-scope="cell">
        {{cell.item.questions_and_answers.length}}
      </template>
      <template slot="operations" slot-scope="cell">
        <b-button-toolbar>
          <b-button-group class="mx-1">
            <b-button type="submit" variant="primary" v-on:click="play(cell.index)">
              <v-icon name="regular/play-circle" scale="1.5"/>
            </b-button>
          </b-button-group>
        </b-button-toolbar>
      </template>
    </b-table>
  </div>
</template>

<script>
import Vue from 'vue'
import VueResource from 'vue-resource'
import store from '../Profile'


export default {
  name: 'ListQuizes',
  data() {
    return {
      quizes: [],
      fields: ["name", "questions", "operations"]
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
    },
    play(quiz) {
      this.$router.push({name: 'play', params: { name: this.quizes[quiz].name }});
    }
  }
}

</script>

<style scoped>
</style>
