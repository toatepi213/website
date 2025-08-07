from Question import Question

question_prompts = [
    "Where was Israel Adesanya born?\nA. America\nB. Australia\nC. Nigeria\nD. Jamaica\n\n",
    "Where does he reside?\nA. America\nB. New Zealand\nC. Nigeria\nD. Jamaica\n\n",
    "What is he famous for?\nA. WWE\nB. Boxing\nC. Kickboxing\nD. UFC\n\n",
    "What is his record in UFC?\nA. 24-3-0\nB. 26-8-9\nC. 12-2-0\nD. 24-0-3\n\n",
    "Who is his trainer?\nA. Cordae Tuigamala\nB. Eugene Bareman\nC. Tenaki Masters\nD. Eugene Baremen\n\n",
    "What age did Israel start fighting?\nA. 19\nB. 14\nC. 16\nD. 18\n\n",
    "What is Israel Adesanya's nickname?\nA. The Beast\nB. The Dog\nC. The Last Stylebender\nD. Slender Machine\n\n"
]

questions = [
    Question(question_prompts[0], "C"),
    Question(question_prompts[1], "B"),
    Question(question_prompts[2], "D"),
    Question(question_prompts[3], "A"),
    Question(question_prompts[4], "B"),
    Question(question_prompts[5], "D"),
    Question(question_prompts[6], "C")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer.upper() == question.answer:
            score += 1
    print("Well Done! You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)
