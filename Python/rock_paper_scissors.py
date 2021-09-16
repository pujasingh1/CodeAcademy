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
games_image = [rock, paper, scissors]
choose = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors \n"))

if choose >= 3 or choose < 0:
  print("You typed a invalid number, You lose😓")
else:
  print(games_image[choose])

  computer_choose = random.randint(0, 2)
  print("Computer Choose: \n")
  print(games_image[computer_choose])

  if choose == 0 and computer_choose == 2:
    print("You Win😍")
  elif computer_choose == 0 and choose == 2:
    print("You lose😓")
  elif choose > computer_choose:
    print("You Win😍")
  elif computer_choose > choose:
    print("You lose😓")
  elif choose == computer_choose:
    print("It's a Tie🤨")
