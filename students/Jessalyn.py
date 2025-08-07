# Python quiz game 

 

from socket import SOCK_STREAM 

 

 

questions = ("What is Kate Sheppard Famous for?", 

             "What was Kate Sheppard protesting about?", 

             "What challenges did Kate Sheppard face?", 

             "When did Kate Sheppard protest?", 

             "What was Kate job (before)?", 

             "What inspired Kate Sheppard?", 

             "Why was Kate Sheppard picked to be on the 10 Dollar note?", 

             "Kate Sheppard was known to be a...", 

             "What dose WCTU stand for?", 

             "What is Kate Sheppard date of birth and death?",) 

 

options = (("A. Writing books", "B.  Song writer", "C. Leader", "D. Making clothes"), 

           ("A. Giving women rights", "B.  Giving rights to black people", "C. Pay rise", "D. Freedom"), 

           ("A.  Voting and politics as domain of men", "B.  Not to be killed", "C. Fear ", "D.  Sickness "), 

           ("A. 1890", "B.   1740", "C. 1630", "D. 1885 "), 

           ("A. making Clothes", "B.  Editor - “the white Ribbon", "C. Cutting down trees", "D. Nurse"), 

           ("A. Justice", "B. God", "C. Help", "D. Her Father"), 

           ("A.  Leader", "B. Church", "C. Smart", "D.  Rich"), 

           ("A. Feminist", "B.  Prettiest", "C. Poorest", "D. Best Singer"), 

           ("A. Women cannot touch you", "B.  Wales cannot stand up", "C. Women Chistian temperance union", "D. Want can tin up"), 

           ("A. 12.06.47 - 20.03.22", "B.  03.09.50 - 10.12.10", "C. 12.10.16 - 10.11.20", "D. 10.11.47 - 13.10.34"),) 

 

answers = ("C", "A", "A", "D", "B","A", "A", "A", "C", "D") 

guesses = [] 

score = 0 

questions_num = 0   

 

for question in questions: 

    print("-----------------------") 

    print(question) 

    for option in options[questions_num] : 

        print(option) 

 

    guess = input("Enter (A, B, C, D): ").upper() 

    guesses.append(guess) 

    if guess == answers[questions_num]: 

        score += 1 

        print("CORRECT!")  

    else: 

        print("INCORRECT!") 

        print(f"{answers[questions_num]} is the correct answer") 

    questions_num += 1 

 

print("-----------------------") 

print("       RESULTS         ") 

print("-----------------------") 

 

print("answers:", end="") 

for anwer in answers: 

    print(anwer, end=" ") 

print()   

 

print("guesses:", end="") 

for guess in guesses: 

    print(guess, end=" ") 

print()   

 

score = int(score / len(questions) * 100) 

print(f"your score is: {score}%") 