# python quiz game

questions = (
    "What is the capital of France?",
    "Which language is primarily used for web development?",
    "What does CPU stand for?",
    "What planet is known as the Red Planet?",
    "Who wrote 'Romeo and Juliet'?",
    "What is the largest ocean on Earth?",
    "Which element has the chemical symbol 'O'?"
)

options = (("A.Berlin", "B. Madrid", "C. Paris", "D. Rome"),("A. Python", "B. JavaScript", "C. C++", "D. Java"),("A. Central Performance Unit", "B. Central Processing Unit", "C. Computer Personal Unit", "D. Control Processing Unit"),("A.Venus", "B. Mars", "C. Jupiter", "D. Saturn"),("A. William Shakespeare", "B. Charles Dickens", "C. Leo Tolstoy", "D. Mark Twain")
            ,("A. Atlantic Ocean", "B. Indian Ocean", "C. Pacific Ocean", "D. Arctic Ocean"),("A. Oxygen", "B. Gold", "C. Silver", "D. Hydrogen"))


answers = ("C", "B", "B", "B", "A", "C", "A")
guesses = []
score = 0


question_num = 0

for question in questions:
    print("---------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter your option A,B,C,D: ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score+=1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer!")
    question_num+=1

print("----------------------")
print("       Results        ")
print("----------------------")

print("answers: ",end="")
for answer in answers:
    print(answer,end=" ")
print()


print("guesses: ",end="")
for guess in guesses:
    print(guess)

print()


score = int(score / len(questions) * 100)

print(f"your score is: {score}%")
