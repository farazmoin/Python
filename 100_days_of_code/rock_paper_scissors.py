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

# Variables
choices_list = [rock, paper, scissors]
user_choice = int(input('What do you chose? Type 0 for Rock, 1 for Paper, and 2 for Scissor'))
computer_choice = random.randint(0, 2)

# Conditional block
if user_choice == computer_choice:
    print('Draw')
else:
    if user_choice >= 3:
        print('Chose a number between 0 and 2')
    else:
        print(choices_list[user_choice])
        print('Computer chose:\n', choices_list[computer_choice])
    if user_choice == 0 and (computer_choice == 2):
        print('You win')
    elif user_choice == 0 and (computer_choice == 1):
        print('You lose')
    if user_choice == 1 and (computer_choice == 2):
        print('You lose')
    elif user_choice == 1 and (computer_choice == 0):
        print('You win')
    if user_choice == 2 and (computer_choice == 1):
        print('You win')
    elif user_choice == 2 and (computer_choice == 0):
        print('You lose')