from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

#-------Creating Object by 'Question' class and store every object into a list---------------
questions = question_data[0]["results"]
for question in questions:
    question_bank.append(Question(question['question'],question['correct_answer']))

quiz = QuizBrain(question_bank)

while quiz.has_question():
    quiz.next_question()
    if quiz.question_number == len(question_bank):
        print("\n-----------------------------\n")
        print("You've completed the quiz")
        print(f"Your final score was : {quiz.score}/{quiz.question_number}")
