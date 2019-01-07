<template>
  <div>
    <h1>Create a new quiz</h1>
    <h2 v-if="isNamed">{{name}}</h2>
    <span v-else>
      <label for="quizName">Enter the name of the quiz:&nbsp;</label>
      <input id="quizName" type="text" v-model="name">
      <button v-on:click="nameQuiz">Create</button>
    </span>
    <ol>
      <li v-for="question in questions">{{question.q}} - {{question.a}}</li>
    </ol>
  </div>
</template>

<script>
export default {
  name: 'CreateQuiz',
  data() {
    return {
      name: "",
      questions: [
      {
        q: "Who is Luke's father?",
        a: "Darth Vader"
      },
      {
        q: "What planet lies at your bottom?",
        a: "Your anus"
      }
    ],
      isNamed: false
    }
  },
  methods: {
    nameQuiz() {
      console.log("Create a new quiz named " + this.name);
      this.isNamed = true;
    }
  }
}
</script>

<style scoped>
</style>
