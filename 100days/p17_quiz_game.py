from p17_data import question_data
from p17_question_model import Question
from p17_quiz_brain import QuizBrain

question_bank = []
	
for key in question_data:
	question_bank.append(Question(key["text"], key["answer"]))

# print(question_bank)
# print(question_bank[0].text)
# print(question_bank[0].answer)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
	quiz.next_question()

print(f"You've completed the quiz. Your final score is {quiz.score}/{len(quiz.question_list)}.")