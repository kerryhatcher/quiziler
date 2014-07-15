__author__ = 'khatch'

import yaml
import random


class StartQuiz():
    question = ""
    questions = ""
    answer = ""
    answers = ""

    def __init__(self):
        self.loadquestions()

    def loadquestions(self, qfile="quesitonbank/questions.yaml"):
        f = open(qfile)
        # use safe_load instead load
        self.questions = yaml.safe_load(f)
        f.close()

    def randomquestion(self):
        qnumber = random.randint(1, 2)
        self.question = self.questions[qnumber]['text']
        self.answer = self.questions[qnumber]['Answer']
        self.answers = self.questions[qnumber]['Answers']