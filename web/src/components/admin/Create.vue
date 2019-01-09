<template>
  <div>
    <h1>Create a new quiz</h1>
    <h2 v-if="isNamed">{{name}}</h2>
    <span v-else>
      <label for="quizName">Enter the name of the quiz:&nbsp;</label>
      <input id="quizName" type="text" v-model="name">
      <button v-on:click="nameQuiz">Create</button>
    </span>
    <b-table :items="questions" :fields="fields">
      <template slot="index" slot-scope="data">
        {{data.index + 1}}
      </template>
      <template slot="text" slot-scope="cell">
        <span v-if="cell.index == indexToEdit">
          <input type="text" v-model="question.text" />
        </span>
        <span v-else>
          {{cell.item.text}}
        </span>
      </template>
      <template slot="operations" slot-scope="cell">
        <b-button-toolbar v-if="cell.index == indexToEdit">
          <b-button-group class="mx-1">
            <b-button type="submit" variant="success">
              <v-icon name="regular/check-circle" scale="1.5"/>
            </b-button>
          </b-button-group>
          <b-button-group class="mx-1">
            <b-button type="submit" variant="danger" v-on:click="cancelEditQuestion">
              <v-icon name="regular/times-circle" scale="1.5"/>
            </b-button>
          </b-button-group>
        </b-button-toolbar>
        <b-button-toolbar v-else>
          <b-button-group class="mx-1">
            <b-button type="submit" variant="danger" v-on:click="removeQuestion(cell.item)">
              <v-icon name="regular/trash-alt" scale="1.5"/>
            </b-button>
          </b-button-group>
          <b-button-group class="mx-1">
            <b-button type="submit" variant="warning" v-on:click="editQuestion(cell.index)">
              <v-icon name="regular/edit" scale="1.5"/>
            </b-button>
          </b-button-group>
          <b-button-group class="mx-1">
            <b-button type="submit" variant="primary" v-if="cell.index > 0" v-on:click="moveUp(cell.index)">
              <v-icon name="regular/caret-square-up" scale="1.5"/>
            </b-button>
            <b-button type="submit" variant="primary" :disabled="isLastRow(cell.index)" v-on:click="moveDown(cell.index)">
              <v-icon name="regular/caret-square-down" scale="1.5"/>
            </b-button>
          </b-button-group>
        </b-button-toolbar>
      </template>
    </b-table>
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
        <b-button type="submit" variant="success">
          <v-icon name="regular/plus-square" scale="1.5"/>
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
      indexToEdit: -1,
      questions: [],
      question: {},
      fields: ["index", "text", "answer", "operations"]
    }
  },
  methods: {
    nameQuiz() {
      this.isNamed = true;
    },
    isLastRow(index) {
      return index == this.questions.length-1;
    },
    addQuestion() {
      this.questions.push({
        text: this.question.text,
        answer: this.question.answer
      });
      this.question = {};
    },
    editQuestion(index) {
      this.indexToEdit = index;
      this.question = this.questions[index];
    },
    cancelEditQuestion() {
      this.indexToEdit = -1;
      this.question = {};
    },
    removeQuestion(question) {
      this.questions.splice(question, 1);
    },
    moveDown(index) {
      this.questions[index] = this.questions.splice(index+1, 1, this.questions[index])[0];
    },
    moveUp(index) {
      this.questions[index-1] = this.questions.splice(index, 1, this.questions[index-1])[0];
    }
  }
}
</script>

<style scoped>
</style>
