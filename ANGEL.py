# python Quiz Game
 
questions = ("Who is the lady found on the ten-dollar bill?: ",
            "How many husbands did Kate Sheppard have?: ",
            "What was the date of Kate's death?: ",
            "Where was Kate Sheppard born?: ",
            "What was Kate Sheppard's sister's name?: ")
 
options = (("A. Emily Davison", "B. Matilda Joslyn Gage", "C. Kate Sheppard", "D. Abby Kelley Foster"),
           ("A. 1", "B. 3", "C. 2", "D. none"),
           ("A. 3rd November 1936", "B. July 13th", "1934, C. March 22nd, 1933", "D. 10th May 1929"),
           ("A. Liverpool, England", "B. Wellington, New Zealand", "C. Glasgow, Scotland", "D. Plovdiv, Bulgaria"),
           ("A. Jane May", "B. Elizabeth May", "C. She didn't have a sister", "D. Isabella May"))
 
answers = ("C", "C", "B", "A", "D")
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
        print("Good Try! But not quite.")
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
 