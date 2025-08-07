# Asking to put your name in order to play the quiz
name = input("Hi, What is your name? ")

if name == "sub":
    print(name + " ")

# Welcomes you into the quiz
print("Welcome " + name + " to the Hunt for the wilderpeople quiz")

# Function to initiate quiz participation
def quiz_participation():
    response = input("Do you want to participate in my quiz? (yes/no): ").lower()
    if response == "yes":
        print("Great! Let's start the quiz.")
    elif response == "no":
        print("No problem. Maybe next time!")
        exit()  # Exit the program if the user doesn't want to participate
    else:
        print("Invalid response. Please enter 'yes' or 'no'.")
        quiz_participation()  # Recursive call to ensure valid response

# Call the function to initiate quiz participation
quiz_participation()

# Questions that will be asked
questions = (
    "Who was the main character in the movie hunter for the wilder people?: ",
    "How old was Ricky baker?: ",
    "Why did rickys parents abandoned him?: ",
    "What is the favourite saying of Paula, the child protection officer?: ",
    "What book is Hunt for the wilder people based off?: ",
    "Why does Hec not like when Ricky calls him uncle?: ",
    "How does Bella break through Rickys protective shield?: ",
    "What did Hec serve time in prison for?: ",
    "When Bella dies, what happens next?: ",
    "Why is Ricky scared of going to juve?:",
)

# Options for each question
options = (
    ("A. Rickey Baker", "B. Hec", "C. Paula", "D. Bella"),
    ("A. 16", "B. 13", "C. 12", "D. 15"),
    ("A. Because they were too young", "B. financial problems", "C. Homeless", "D. Bad parenting"),
    ("A. Lock 'em up", "B. No child left behind", "C. For all the left behind children", "D. For whanau, for children"),
    ("A. Wild pork and wildercress", "B. Ricky baker and Uncle Hec", "C. Hunt for the wilderpeople", "D. Man alone"),
    ("A. He doesn't like people trying to get close to him", "B. he thinks ricky is annoying", "C. He likes his own name, hector", "D. He hates that name"),
    ("A. She takes him hunting", "B. She gives him a dog, tupac, and sings him a song", "C. She reads to him", "D. she gives him a present"),
    ("A. Murder", "B. Manslaughter", "C. Kidnapping", "D. Theft"),
    ("A. Ricky runs away", "B. Ricky fakes his suicide", "C. Ricky burns down the barn", "D. A letter arrives from child welfare services saying that Ricky has to leave"),
    ("A. No", "B. Maybe", "C. Yes", "D. very sure")
)

# Correct answers for each question
answers = ("A", "A", "B", "A", "A", "B", "B", "D", "A", "A")

# List to store user's guesses
guesses = []

# Initialize score counter
correct_answers = 0

# Iterate over each question
for index, question in enumerate(questions):
    print("----------------------")
    print(question)
    for option in options[index]:
        print(option)

    # Get user input and validate
    while True:
        guess = input("Enter your answer (A, B, C, D): ").strip().upper()
        if guess in ["A", "B", "C", "D"]:
            break
        else:
            print("Invalid input! Please enter A, B, C, or D.")

    # Record user's guess
    guesses.append(guess)

    # Check if user's guess is correct
    if guess == answers[index]:
        correct_answers += 1
        print("That is correct!!")
    else:
        print("That is wrong")
        print(f"{answers[index]} is the right answer")

# Calculate percentage of correct answers
percentage_correct = (correct_answers / len(questions)) * 100

# Display results
print("---------------------")
print("       RESULTS       ")
print("---------------------")
print("Answers:", " ".join(answers))
print("Guesses:", " ".join(guesses))
print(f"Percentage correct: {percentage_correct}%")

print("Thank you for playing my quiz!")


