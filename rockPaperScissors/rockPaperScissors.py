from lib2to3.fixes.fix_input import context

from select import select

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

import random
computerChoice = random.randint(0, 2)
game = [rock, paper, scissors]

userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors!\n"))

if userChoice >= 0 and userChoice <= 2:
    print(game[userChoice])
    print("Computer chose:")
    print(game[computerChoice])

if userChoice < 0 or userChoice > 2:
    print("You typed an invalid number, you lose!")
elif userChoice == computerChoice:
    print("It's a draw!")
elif userChoice == 0 and computerChoice == 2:
    print("You Win!")
elif userChoice == 2 and computerChoice == 0:
    print("You Lose!")
elif userChoice > computerChoice:
    print("You Win!")
else:
    print("You Lose!")
