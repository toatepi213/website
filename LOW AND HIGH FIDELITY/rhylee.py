# Python quiz game 

# This welcomes you to my quiz 

name = input("Hello what is your name?") 

#include the name of the user to engage him/her
playing = input(f"{name}, do you want to participate in this quiz about Israel Adesanya? (yes/no): ").lower() 


if playing == "yes": 

    #This welcomes you to the quiz with your name 

    print("Hello {} Welcome to a quiz about Israel Adesanya, this quiz can help you learn more about him" .format(name)) 

 

# Questions 

questions = ("What title did Israel Adesanya win in the UFC 287?: ", 

            "Who did Israel Adesanya defeat to win the UFC Middleweight title in October 2019?: ", 

            "In which country was boxer Israel Adesanya born?: ", 

            "Which brazilian kickboxer beat Israel Adesanya at UFC 281?: ", 

            "Which former UFC middleweight champion lost his title to Israel Adesanya in February 2019?: ", 

            "Which gym does Israel Adesanya train at?") 

# Options 

options = (("A. UFC Middleweight championship", "B. UFC Lightweight championship", "C. UFC Lightheavyweight championship", "D. UFC Heavyweight championship"), 

           ("A. George St-Pierre", "B. Mike Tyson", "C. Robert Whittaker", "D. Michael Jackson"), 

           ("A. China", "B. Nigeria ", "C. Ireland", "D. Ghana"), 

           ("A. Jose Aldo", "B. Charles Olivera", "C. Anderson Silva", "D. Alex Pereira"), 

           ("A. Anderson Silva", "B. Lebron James", "C. Paulo Costa", "D. Sean Strickland"), 

           ("A. Auckland MMA", "B. The combat centre", "C. Oliver MMA HQ", "D. City Kickboxing")) 

# Correct answers 

answers = ("A", "C", "B", "D", "A") 

guesses = [] 

score = 0 

question_num = 0 

# For question in questions 

for question in questions: 

    print("----------------------") 

    print(question) 

    for option in options[question_num]: 

        print(option) 

# Input answers 

    guess = input("Enter (A, B, C, D): ").upper() 

    guesses.append(guess) 

    if guess == answers [question_num]: 

        score += 1 

        print("CORRECT!") 

    else: 

            print("INCORRECT!") 

            print(f"{answers[question_num]} is the correct answer") 

    if  len(option) == 0 or   len(option) >= 2: 

            print("Please enter a valid answer\n")  

            continue 

    else:  

          break 

    question_num += 1 

    question_num += 1 

# Results 

print("----------------------") 

print("      RESULTS     ") 

print("----------------------") 

         

print("answers: ", end="") 

for answer in answers: 

    print(answer, end=" ") 

print() 

 

print("guesses: ", end="") 

for guess in guesses: 

    print(guess, end=" ") 

print() 

         

# Scoring systems 

score = (score / len(questions) * 100) 

print(f"Your score is: {score}%") 

 
