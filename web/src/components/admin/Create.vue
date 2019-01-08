<template>
  <div>
    <h1>Create a new quiz</h1>
    <h2 v-if="isNamed">{{name}}</h2>
    <span v-else>
      <label for="quizName">Enter the name of the quiz:&nbsp;</label>
      <input id="quizName" type="text" v-model="name">
      <button v-on:click="nameQuiz">Create</button>
    </span>
    <b-list-group>
      <b-list-group-item v-for="(question, index) in questions">
        {{index+1}} : {{question.text}} - {{question.answer}}
      </b-list-group-item>
    </b-list-group>
    <div>
      <b-form @submit="addQuestion" inline>
        <label class="mr-sm-2" for="textInput">Question:</label>
        <b-form-input id="textInput"
                      class="mb-2 mr-sm-2 mb-sm-0"
                      type="text"
                      v-model="question.text"
                      required
                      placeholder="Enter the question">
        </b-form-input>
        <b-form-input id="answerInput"
                      class="mb-2 mr-sm-2 mb-sm-0"
                      type="text"
                      v-model="question.answer"
                      required
                      placeholder="Enter the answer">
        </b-form-input>
        <b-button type="submit" variant="primary">
          Add
          <span class="glyphicon glyphicon-envelope"></span>
        </b-button>
      </b-form>
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
