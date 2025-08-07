# Python quiz game
 
questions = ("Who is Archibald Hector McIndoe ?: ",
             "What did Archibald McIndoe discover?: ",
             "What did McIndoe understand the importance of?: ",
             "What year did Sir Archibald Hector McIndoe  worked for the Royal Air Force during the Second World War ?: ",
             "How did Archbald Hector Mcindoe died?",
             "What did Archibald McIndoe invent?: ",
             "How did he became well known ?: ",
             "What year did he died ?: ",
             "Where is he from?: : ")
 
options = (("a. A  prime minister ","b. New Zealand mountaineer ","c. Actor - Comedian","d. Surgeon"),
           ("a. He discovered and mapped normal and pathological blood supply to the liver.","b.  An abnormal condition that affects the structure or function part of the body and is usually associated with specific signs and symptoms.","c. ribose-5-phosphate isomerase deficiency is considered the 2nd rarest known genetic disease being beaten only by Fields Condition affecting two known individuals, Catherine and Kirstie Fields. "),
           ("a. The treatment for flu and diseases","b. pioneering treatment of burns victims during the Second World War revolutionized the field of plastic surgery","c. pioneering treatment of burns victims during the Second World War revolutionized the field of plastic surgery", "d. Suicide"),
           ("a. 4 May 1900 - 11 April 1960","b.  2 June 1930-8 Oct 1946","c. 26 April 1820-2 Jul 1842", "d. Suicide"),
           ("1. From a house fire","2. Murdered","3.  Heart attack","4. Suicide"),
           ("1. A new medicine for heart attack","2. new techniques for treating badly burned faces and hands","3. How to treat injured or bruised part of the body"),
           ("a. Greatly improved the treatment and rehabilitation of badly burned aircrew","b. By helping and to cure people with severe injure ","c. Having a new ways or ideas to cure people"),
           ("1. 1972","2. 1964","3. 1960","4. 1970","5. 1989"),
           ("a. Argentina","b. New York City","c. Forbury, in Dunedin, New Zealand","d. Prestatyn, North Wales"))
 
answers = ("d","a","b","a","3","2","a","3","c")
guesses = []
score = 0
question_num = 0
 
for question in questions:
    print("------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
 
    guess = input("Enter (a,b,c,d,1,2,3,4)").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    
    question_num += 1
 
print("------------------------")
print("        RESULTS         ")
print("------------------------")
 
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