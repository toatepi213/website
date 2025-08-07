# Python quiz game   

 

name = input("What is your name?: ") 

age = int(input("How old are you?: ")) 

 

print("Hello "+name) 

print("You are "+str(age)+" years old") 

questions = ("Who is Lorde?: ", 

             "When was she born?: ", 

             "What was her original name?: ", 

             "How many siblings does she have?: ", 

             "Where was she born?: ", 

             "Which one of her songs sold 10 million units worldwide?: ", 

             "What year did Lordes parents got married?: ", 

             "How old was Lorde when she signed a development contract with Universal Music Group?: ", 

             "This 2024, How old do you think she is?: ", 

             "How many songs does Lorde have?: ") 

 

options = (("A. Actor","B. Comedian","C. Singer","D. Dancer"), 

           ("A. December 13,1989","B. March 2,1996","C. August 17,2000","D. November 7,1996"), 

           ("A. Sandy Rose Yelich-O'Connor","B. Ella Marija Lani Yelich-O'Connor","C. Ruby Jane Yelich-O'Connor","D. Lorde Yelich-O'Connor"), 

           ("A. 3","B. 4","C. 7","D. 1"), 

           ("A. Sydney,Australia","B. Toronto,Canada","C. Takapuna,Auckland","D. San Francisco,USA"), 

           ("A. Moonlight","B. Team","C. Everyday","D. Royals"), 

           ("A. 2009","B. 1990","C. 2017","D. 1890"), 

           ("A. 10","B. 14","C. 12","D. 31"), 

           ("A. 19","B. 33","C. 28","D. 24"), 

           ("A. 101","B. 300","C. 200","D. 202")) 

 

answers = ("C", "D", "B", "A", "C", "D", "C", "C", "C", "D") 

guesses = [] 

score = 0 

question_num = 0 

 

for question in questions: 

    print("----------------------") 

    print(question) 

    for option in options[question_num]: 

        print(option) 

 

    guess = input("Enter (A, B, C, D,): ").upper() 

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

