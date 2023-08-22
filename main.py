# Day-4: Project: Rock, Paper, Scissors
# Rock = 0
# Paper = 1
# Scissors = 2

# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.


import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice >= 3 or user_choice < 0:
  print("Invalid Input. Try again.")
else:
  print(f"You chose:\n{game_images[user_choice]}")

computer_choice = random.randint(0, 2)
print(f"Computer chose:\n{game_images[computer_choice]}")


if user_choice == computer_choice:
  print("It's a draw!")
# Rock wins against scissors.
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
# Scissors win against paper.
elif user_choice == 2 and computer_choice == 1:
  print("You win!")
# Paper wins against rock.
elif user_choice == 1 and computer_choice == 0:
  print("You win!")
else:
  print("You lose! Computer wins!")
