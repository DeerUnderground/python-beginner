import random

import os

from art import logo

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

def deal_card():
  return random.choice(cards)

def calculate_score(lis):
  if sum(lis)== 21 and len(lis)==2:
    return 0
  elif sum(lis)>21 and 11 in lis:
    lis.remove(11)
    lis.append(1)
    return sum(lis)
  else:
    return sum(lis)
    
def compare(lis1, lis2):
  print(f"Your cards are {user_cards}")
  print(f"Computer's cards are {comp_cards}")
  if sum(lis1)== sum(lis2):
    print("It's a draw!")
  elif calculate_score(lis2)==0:
    print("you lose")
  elif calculate_score(lis1)==0:
    print("you win")
  elif calculate_score(lis1)>21:
    print("You lose")
  elif calculate_score(lis2)>21:
    print("You win")
  else:
    if calculate_score(lis1) > calculate_score(lis2):
      print("You win")
    else:
      print("You lose")
inp1 = input("wanna play some blackjack?\n")
while inp1 == "y":
  os.system('clear')
  print(logo)
  user_cards = []
  comp_cards = []
  user_cards.append(deal_card())
  user_cards.append(deal_card())
  comp_cards.append(deal_card())

  game_cont = True
  while game_cont:
    print(f"Your cards are {user_cards}")
    print(f"Computer's cards are {comp_cards}")
    if calculate_score(user_cards)==0:
      game_cont = False
    elif calculate_score(user_cards)>21:
      game_cont = False
    else:
      cont = input("want to continue playing?\n")
      if cont == "y":
        user_cards.append(deal_card())
      elif cont == "n":
        game_cont= False
  while calculate_score(comp_cards)<17:
    comp_cards.append(deal_card())
  compare(user_cards, comp_cards)
  inp1 = input("wanna continue playing? y or n\n")
