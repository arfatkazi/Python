# import random


# low = 1
# high = 100

# options = ('rock','paper','scissor')
# number = random.randint(low,high)


# choices = random.choice(options)


# # print(number)


# # print(random.random())


# print(choices)




# Random number guessing
# import random

# lowest_num = int(input("Enter your number: "))
# highest_num = int(input("Enter your number: "))

# secret_number = random.randint(lowest_num,highest_num)



# guesses = 5


# print(f"\n🎯 I have picked a number between {lowest_num} and {highest_num}. You have {guesses} guesses!")


# while guesses > 0:
#     guess = int(input("Enter your guess: "))


#     if guess == secret_number:
#          print("🎉 Congratulations! You guessed the correct number!")
#          break
    
   

#     elif guess < secret_number:
#             print("📉 Too low!")
    
#     elif guess > secret_number:
#             print("📉 Too high!")


#     guesses -= 1
#     print(f"❗ You have {guesses} guess(es) left.\n") 

# if guesses == 0:
#     print(f"💀 You've run out of guesses. The number was {secret_number}. Better luck next time!")      



# ROCK,PAPER,SCISSOR

# import random

# options = ['rock', 'paper', 'scissors']

# print("Welcome to the rock, paper, scissor game 🎮!")

# while True:
#     user_choice = input("Choose rock, paper, or scissors (or 'q' to quit): ").lower()

#     if user_choice == 'q':
#         print("👋 Thanks for playing!")
#         break

#     if user_choice not in options:
#         print("❌ Invalid choice. Try again.")
#         continue

#     computer_choice = random.choice(options)
#     print(f"🧠 Computer chose: {computer_choice}")

#     if user_choice == computer_choice:
#         print("🤝 It's a tie!")

#     elif (
#         (user_choice == "rock" and computer_choice == "scissors") or
#         (user_choice == "paper" and computer_choice == "rock") or
#         (user_choice == "scissors" and computer_choice == "paper")
#     ):
#         print("🎉 You win!")
#     else:
#         print("💻 Computer wins!")

#     print()  


# dice roll

import random

# Unicode dice face graphics
dice_faces = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"
    ),
}

# Rolling dice
dice = []
total = 0
num_of_dice = int(input("🎲 How many dice?: "))

for die in range(num_of_dice):
    roll = random.randint(1, 6)
    dice.append(roll)
    total += roll

# Print dice faces side by side
dice_art = [""] * 5
for roll in dice:
    face = dice_faces[roll]
    for i in range(5):
        dice_art[i] += face[i] + "  "

print("\nYour Dice Roll:")
for line in dice_art:
    print(line)

print(f"\n🔢 Total: {total}")
