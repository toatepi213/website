#This is to input a name 
name = input("Hello! What is your name? ")

if name == "sub":
    print(name + " ")

#These are the list of questions
print("Welcome, " + name +" to My quiz on an iconic New Zealander! Regan Roell!")
questions = ("Where is Regan Roell from?: ",
             "What is Regan Roell famous for?: ",
             "When was Regan Roell born?: ",
             "What is Regan Roell’s real name? :",
             "How currently old is Regan Roell?:",
             "What ethnicity is Regan Roell?: ",
             "True or False: Regan and NBA YoungBoy were born on the same day: ",
             "True or False: Regan is a song producer:  ",
             "Where was Regan Roell raised?: ",
             "Which one of the songs did Regan release?: ",)

#These are the options of answers
options = (("A. USA ", "B. Spain ", "C. Australia  ", "D. New Zealand "),
           ("A. Being a singer ", "B. Social media influencer ", "C. Health influencer", "D. Being rich"),
           ("A. October 20, 1989 ", "B. May 9, 2000", "C. July 20, 1991 ", "D. January 11, 1973 "),        
           ("A. Regan Walkins ", "B. Regan Siasi ", "C. Regan Foai ", "D. Regan Miller"),        
           ("A. 24 ", "B. 27 ", "C. 36 ", "D. 34 "),        
           ("A. Māori ", "B. Tongan ", "C. Hawaiian  ", "D. Niuean "),        
           ("A. True ", "B. False"),        
           ("A. True", "B. False"),        
           ("A. Palmerston North", "B. Christchurch ", "C. Auckland", "D. Gisborne  "),        
           ("A. Drinkin’ problem ", "B. We aint gotta rush ", "C. Love again", "D. Ouana"))        

#These are the correct answers
answers = ("D", "B", "A", "C", "D", "D", "A", "A", "C", "B")
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
        print("ding! Thats correct!")
    else:
        print("Errr- Thats incorrect!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("-----------------------------")
print("╔═══╦═══╦═══╦╗ ╔╦╗ ╔════╦═══╗")
print("║╔═╗║╔══╣╔═╗║║ ║║║ ║╔╗╔╗║╔═╗║")
print("║╚═╝║╚══╣╚══╣║ ║║║ ╚╝║║╚╣╚══╗")
print("║╔╗╔╣╔══╩══╗║║ ║║║ ╔╗║║ ╚══╗║")
print("║║║╚╣╚══╣╚═╝║╚═╝║╚═╝║║║ ║╚═╝║")
print("╚╝╚═╩═══╩═══╩═══╩═══╝╚╝ ╚═══╝")
print("-----------------------------")

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


