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

rps = [rock, paper, scissors] 
#rps - rock, paper, scissor all in one list 


choice_number = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors"))
computer_choice = random.randint(0,2)

if choice_number >=3 and choice_number <0: 
  print("You lose. Because of invalid number")
 

else:
  print("User chose") 
  print(rps[choice_number]) 

print("Computer chose")
print(rps[computer_choice])

if choice_number == computer_choice: 
  print("No winner.")  

elif choice_number == 0: 
  if computer_choice == 1: 
    print("you Lose")
  else: 
    print("you win!")    

elif choice_number == 1: 
  if computer_choice == 0: 
    print("You win!")
  else: 
    print("You Loose")

elif choice_number == 2: 
  if computer_choice == 1: 
    print("you win")
  else: 
    print("You loose")
else: 
  print("Please enter the proper value") 


