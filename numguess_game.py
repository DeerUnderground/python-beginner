import random

from art import logo

ran_number = random.randint(1,100)
print(logo)
print("would you like to play the game in")
level = input("easymode/hardmode/impossiblemode\n")

if level == "easymode":
  lives = 10
elif level == "hardmode":
  lives = 5
else:
  lives = 2
  
def check_guess(num):
  global lives
  if num==ran_number:
    print("you win lol")
    lives = 0
  elif num > ran_number:
    print("too high")
    lives -= 1
    if lives == 0:
      print("you lose")
  else:
    print("too low")
    lives -= 1
    if lives == 0:
      print("you lose")
while lives > 0:
  guess = int(input("guess a num between 1 and 100\n"))
  check_guess(guess)


# while lives > 0:
#   guess = int(input("guess a # between 1 and 100:\n"))
#   if guess== ran_number:
#     print("you win!!! wow")
#     lives = 0
#   elif guess > ran_number:
#     print("your guess was too high, try again")
#     lives -= 1
#     print(f"you have {lives} lives remaining")
#   elif guess < ran_number:
#     print("your guess was too low, try again")
#     lives -= 1
#     print(f"you have {lives} lives remaining")
