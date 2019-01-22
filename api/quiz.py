class Quiz:
    def __init__(self, name):
        self.name = name
        self.questions = []

    def add(self, question):
        self.questions.append(question)

    def addAll(self, questions):
        self.questions.extend(questions)

    @classmethod
    def fromDict(cls, dict):
        quiz = cls(dict['name'])
        quiz.addAll(list(map(Question.fromDict, dict['questions'])))
        return quiz

    def __repr__(self):
        return str(self.__dict__)

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    @classmethod
    def fromDict(cls, dict):
        return Question(dict['text'], dict['answer'])

    def __repr__(self):
        return str(self.__dict__)

class Questions:
    def __init__(self, questions):
        self.questions = questions

    @classmethod
    def fromQuizDict(cls, dict):
        return cls(list(map(lambda q: q['text'], dict['questions'])))

    def __repr__(self):
        return str(self.__dict__)
