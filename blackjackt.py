import random 

def deal(): 
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards): 
  """User yoki computer olgan kartalarni hisoblab beradi"""

  if sum(cards) == 21 and len(cards) == 2: 
    return 0
  if 11 in cards and sum(cards)> 21:
    cards.remove(11)
    cards.append(1)

  return sum(cards)

def compare(user_score,computer_score): 
  if user_score == computer_score: 
    return "It is draw!:)" 
  elif computer_score == 0 or user_score > 21: 
    return "Computer wins!:("
  elif user_score == 0 or computer_score > 21:
    return 'User wins!:)'
  elif user_score > computer_score: 
    return "User wins!"
  else: 
    return "You lose. Computer wins"


user_cards = []
computer_cards = []
is_game_over = False

for _ in range(2):
  user_cards.append(deal())
  computer_cards.append(deal())

print(user_cards)
print(computer_cards)


while not is_game_over: 

  user_score = calculate_score(user_cards) 
  computer_score = calculate_score(computer_cards)
  print(f"Your cards{user_cards} and current score:{user_score}")
  print(f"Computer first card:{computer_cards[0]}")


  if user_score == 0 or computer_score == 0 or user_score > 21: 
    is_game_over = True 

  else: 
    extra_card = input("Type 'y' to get another card, type 'n' to pass: ") 

    if extra_card == 'y': 
      user_cards.append(deal())
    else: 
      is_game_over = True

  print(user_cards)

  while computer_score == 0 or computer_score < 17:
    computer_cards.append(deal()) 
    computer_score = calculate_score(computer_cards)

  compare(user_score,computer_score)

  #Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

