class Quiz:
    def __init__(self, name):
        self.name = name
        self.questions = []

    def add(self, question):
        self.questions.append(question)

    def __repr__(self):
        return str(self.__dict__)

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def __repr__(self):
        return str(self.__dict__)
