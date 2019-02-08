import QuizApi from '@/quiz-service'

describe('The Quiz API', () => {
  describe('get all quizes', () => {
    beforeEach(() => {
      const interaction = {
        uponReceiving: 'get all quizes',
        withRequest: {
          method: 'GET',
          path: '/quiz',
          headers: {
            Accept: 'application/json, text/plain, */*'
          }
        },
        willRespondWith: {
          status: 200,
          headers: {
            'Content-Type': 'application/json'
          },
          body: [{
              name: "This is my quiz",
              questions_and_answers: [{
                answer: "On the south pole",
                question: {
                  text: "Where do pinguins live?"
                }
              }]
            },
            {
              name: "Planetary quiz",
              questions_and_answers: [{
                answer: "Mars",
                question: {
                  text: "Which candy circles the sun?"
                }
              }]
            }
          ]
        }
      };
      return provider.addInteraction(interaction);
    });

    it('should return all quizes', done => {
      QuizApi.allQuizes()
        .then(response => {
          expect(response).toHaveLength(2);
        })
        .then(done);
    })
  });

  describe('get one quiz', () => {
    beforeEach(() => {
      const interaction = {
        uponReceiving: 'get one quis',
        withRequest: {
          method: 'GET',
          path: '/quiz/This%20is%20my%20quiz',
          headers: {
            Accept: 'application/json, text/plain, */*'
          }
        },
        willRespondWith: {
          status: 200,
          headers: {
            'Content-Type': 'application/json'
          },
          body: {
            name: "This is my quiz",
            questions_and_answers: [{
              answer: "On the south pole",
              question: {
                text: "Where do pinguins live?"
              }
            }]
          }
        }
      };
      return provider.addInteraction(interaction);
    });

    it('should return one quiz', done => {
      QuizApi.quiz('This is my quiz')
        .then(response => {
          expect(response).toMatchObject({
            "name": "This is my quiz"
          });
        })
        .then(done);
    });
  })
})
