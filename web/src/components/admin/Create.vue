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
      <li v-for="question in questions">{{question.text}} - {{question.answer}}</li>
    </ol>
    <div>
      <label for="question">Enter question:</label>
      <input id="question" type="text" v-model="question.text">
      <label for="answer">Enter answer:</label>
      <input id="answer" type="text" v-model="question.answer">
      <button v-on:click="addQuestion">Add</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CreateQuiz',
  data() {
    return {
      name: "",
      isNamed: false,
      questions: [],
      question: {}
    }
  },
  methods: {
    nameQuiz() {
      this.isNamed = true;
    },
    addQuestion() {
      this.questions.push({
        text: this.question.text,
        answer: this.question.answer
      });
      this.question = {};
    }
  }
}
</script>

<style scoped>
</style>
