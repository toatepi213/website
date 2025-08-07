# Python Quiz Game 

 

questions = ("What does Temuera Morrison do?:",  

             "Which of these movies has he acted in?:", 

             "What year did Temuera Morrison start acting?:", 

             "What ethnicity is Temuera Morrison?:",  

             "What year was Temuera Morrison born?:",  

             "How tall is Temuera Morrison?:", 

             "How old is Temuera Morrison?:",  

             "How many kids does Temuera Morrison have?:", 

             "How many siblings does Temuera Morrison have?:",  

             "Where is Temuera Morrison from?:",) 

 

options = (("A. Act", "B. Sing", "C. Direct", "D. Sportsperson", "E. Model"), 

           ("A. Harry Potter: The Goblet of Fire", "B. Boy", "C. Descendants", "D. The Greenmile", "E. Aquaman"), 

           ("A. 1968", "B. 1973", "C. 1976", "D. 1980", "E. 1984"), 

           ("A. African", "B. British", "C. Tongan", "D. Māori", "E. Other"), 

           ("A. 1958", "B. 1959", "C. 1960", "D. 1961", "E. 1962"), 

           ("A. 1.65m", "B. 1.25m", "C. 1.85m", "D. 1.05m", "E. 1.75m"), 

           ("A. 61", "B. 62 ", "C. 63", "D. 64", "E. 65"), 

           ("A. 5", "B. 10", "C. 0", "D. 1", "E. 3"), 

           ("A. 21", "B. 1", "C. 9", "D. 6", "E. 15"), 

           ("A. Taranaki", "B. Whakatane", "C. Auckland", "D. Rotorua", "E. Christchurch")) 

 

answers = ("A", "E", "B", "D", "C", "E", "C", "E", "B", "D") 

guesses = [] 

score = 0 

question_num = 0 

 

for question in questions: 

    print("-------------------") 

    print(question) 

    for option in options[question_num]: 

        print(option) 

 

    guess = input("Enter (A, B, C, D, E): ").upper() 

    guesses.append(guess) 

    if guess == answers[question_num]: 

        score += 1 

        print("CORRECT!") 

    else: 

        print("INCORRECT!") 

        print(f"{answers[question_num]} is the correct answer") 

    question_num += 1 

 

print("-------------------") 

print("      RESULTS      ") 

print("-------------------") 

 

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