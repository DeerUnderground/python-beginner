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
graphs = [rock, paper, scissors]
comp_move = random.randint(0,2)
print("WELCOME TO THE BATTLEFIELD!")
print("THIS IS A MATTER OF LIFE AND DEATH!")
user_input = int(input("CHOOSE BETWEEN rock (1), paper (2) OR scissors(3)!\n"))
print(graphs[user_input-1])
print("Computer chose...")
print(graphs[comp_move])
if user_input - 1 == comp_move:
	print("IT IS A DRAW!")
else:
	if user_input == 1:
		if comp_move == 1:
			print("YOU LOSE")
		else:
			print("You WIN!")
	elif user_input == 2:
		if comp_move == 0:
			print("You WINNN!")
		else:
			print("You lose ;/")
	else:
		if comp_move == 0:
			print("You lose!")
		else:
			print("YOU WIN!")




