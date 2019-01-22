class Quiz:
    def __init__(self, name):
        self.name = name
        self.questions_and_answers = []

    def add(self, question_and_answer):
        self.questions_and_answers.append(question_and_answer)

    def addAll(self, questions_and_answers):
        self.questions_and_answers.extend(questions_and_answers)

    @classmethod
    def fromDict(cls, dict):
        quiz = cls(dict['name'])
        quiz.addAll(list(map(QuestionAndAnswer.fromDict, dict['questions_and_answers'])))
        return quiz

    def questions(self):
        return list(map(lambda qa: qa.question, self.questions_and_answers))

    def __repr__(self):
        return str(self.__dict__)

class QuestionAndAnswer:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    @classmethod
    def fromDict(cls, dict):
        return cls(Question.fromDict(dict['question']), dict['answer'])

    def __repr__(self):
        return str(self.__dict__)

class Question:
    def __init__(self, text):
        self.text = text

    @classmethod
    def fromDict(cls, dict):
        return cls(dict['text'])

    def __repr__(self):
        return str(self.__dict__)
