print("Who won the super bowl through out the years of 2010-2020") 

  

questions =  ("WHich team won the super bowl in 2011?:", 

             "WHich team won the super bowl in 2012:", 

             "WHich team won the super bowl in 2013?:", 

             "WHich team won the super bowl in 2014?:", 

             "WHich team won the super bowl in 2015?:", 

             "WHich team won the super bowl in 2016?:", 

             "WHich team won the super bowl in 2017?:", 

             "WHich team won the super bowl in 2018?:", 

             "WHich team won the super bowl in 2019?:", 

             "WHich team won the super bowl in 2020?:",) 

 

options = (("A. packers", "B. 49ers ", "C. LA Rams", "D. seahawks"), 

           ("A. Ravens", "B. giants", "C.49ers ", "D. Saints"), 

           ("A.Ravens ", "B. Chiefs", "C.Eagles ", "D. broncos"), 

           ("A.packers ", "B.Raiders ", "C.sea hawks ", "D.cowboys "), 

           ("A.New England ", "B.Sea hawks ", "C.steelers ", "D.dolphins "), 

           ("A. chargers", "B.New England ", "C.bills ", "D.broncos "), 

           ("A. New England", "B.chiefs ", "C.Ravens ", "D. Rams"), 

           ("A. Eagles", "B.New England ", "C.Buccaneers", "D. Vikings"), 

           ("A.Eagles ", "B. New England", "C.Chiefs ", "D. 49ers"), 

           ("A.Bengals ", "B.Browns ", "C.Buffalo Bills ", "D. Buccaneers" ), 

           

          ) 

 

 

 

answers = ("A", "B", "A", "C", "A", "D", "A", "A ", "B", "C", "D", ) 

guesses = [] 

score = 1 

question_num = 0 

 

for question in questions : 

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

 