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

your_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")
your_choice = int(your_choice)

computer_choice = random.randint(0, 2)

if your_choice == computer_choice:
    if your_choice == 0:
        print("Your choice:")
        print(rock)
        print("Computer's choice:")
        print(rock)
        print("Draw!")
    if your_choice == 1:
        print("Your choice:")
        print(paper)
        print("Computer's choice:")
        print(paper)
        print("Draw!")
    if your_choice == 2:
        print("Your choice:")
        print(scissors)
        print("Computer's choice:")
        print(scissors)
        print("Draw!")
    
    

if your_choice == 0 and computer_choice == 1:
    print("Your choice:")
    print(rock)
    print("Computer's choice:")
    print(paper)
    print("You lose!")
if your_choice == 0 and computer_choice == 2: 
    print("Your choice:")
    print(rock)
    print("Computer's choice:")
    print(scissors)
    print("You win!")

if your_choice == 1 and computer_choice == 0: 
    print("Your choice:")
    print(paper)
    print("Computer's choice:")
    print(rock)
    print("You win!")
if your_choice == 1 and computer_choice == 2:
    print("Your choice:")
    print(paper)
    print("Computer's choice:")
    print(scissors) 
    print("You lose!")

if your_choice == 2 and computer_choice == 0:
    print("Your choice:")
    print(scissors)
    print("Computer's choice:")
    print(rock)
    print("You lose!")
if your_choice == 2 and computer_choice == 1:
    print("Your choice:")
    print(scissors)
    print("Computer's choice:")
    print(paper)
    print("You win!")