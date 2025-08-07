# Python quiz game

questions = ("When was Taika Waititi born?: ",
             "Which Marvel movie did Taika Waititi direct?: ",
             "What is the name of Taika Waititi's production company, which he co-founded in 2002 and has produced many of his notable films through?: ",
             "What is the title of Taika Waititi's 2014 film that won the Grand Jury Prize at the Sundance Film Festival?: ",
             "Which of the following films features a character that Taika Waititi did not voice or portray?: ",
             "In which film did Taika Waititi not have a role as an actor or a director?: ",
             "Which of the following languages does Taika Waititi speak fluently?: ",
             "Which of the following is a nickname that Taika Waititi has used or been known by?: ",
             "Which of the following statements about Taika Waititi is true?: ",
             "Which of the following facts about Taika Waititi is true?: ")

options = (("A. 16th July 1974","B. 14th May 1999","C. 16th August 1975","D. 15th May 1973"),
           ("A. Thor: Ragnarok","B. Iron man","C. Black Widow","D. Captain America: The Winter solider"),
           ("A. Piki Films","B. WingNut Films","C. Marvel Studios","D. 20th Century Fox"),
           ("A. Eagle vs Shark","B.  What We Do in the Shadows","C. Hunt for the Wilderpeople","D. Boy"),
           ("A. Thor: Ragnarok","B. Jojo Rabbit","C. What We Do in the Shadows","D. Free Guy"),
           ("A. Thor: Ragnarok","B. Jojo Rabbit","C. The Green Lantern","D. Hunt for the Wilderpeople"),
           ("A. French","B. Spainish","C. Māori","D. Japanese"),
           ("A. T-Wait","B. Taika the Great","C. Taika W.","D. Taika Tiki"),
           ("A. He has a degree in computer science.","B. He has a background in fashion design.","C. He is a vegetarian.","D. He has a daughter named Te Hinekāhu."),
           ("A. He was born in Australia.","B. He has won an Emmy Award for his work.","C. He is a former professional skateboarder.","D.  He was born in New Zealand."))

answers = ("C", "A", "A", "B","D","C", "C", "A", "D", "D")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")