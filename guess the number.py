import random 


number = random.randint(1,100)

def easy_level(): 
  
  attempt = 10 
  print(f"Sizda {attempt}ta jon mavjud") 
  is_game_end = True
  
  while is_game_end: 
    
    user_number = int(input("Taxmin sonningizni kiriting"))
    
    if user_number == number:
      print(f"Siz {number} ni topdingiz. Molodesss!")
      is_game_end = False
      
    
    elif user_number > number: 
      print("Katta! Yana urinib ko'ring ")
      attempt-=1

    elif user_number < number: 
      print("Kichik! Yana urinib ko'ring ")
      attempt-=1

    if attempt == 0: 
      return "Game over"
    print("Sizda {} ta jon qoldi:(".format(attempt))

def hard_level(): 
  attempt = 5
  print(f"Sizda {attempt}ta jon mavjud") 
  is_game_end = True
 
  while is_game_end: 

    user_number = int(input("Taxmin sonningizni kiriting"))
 
    if user_number == number:
      print(f"Siz {number} ni topdingiz. Molodesss!")
      is_game_end = False
      
    
    elif user_number > number: 
      print(f"Katta! Yana urinib ko'ring ")
      attempt-=1

    elif user_number < number: 
      print("Kichik! Yana urinib ko'ring ")
      attempt-=1
      
    if attempt == 0: 
      return "Game over"
    print("Sizda {} ta jon qoldi:(".format(attempt))

choice=input("Sonni topish o'yiniga xush kelibsiz. Man 1 dan 100 gacha son o'yleman. Siz topishingiz kerak.\n Darajani tanglang. 'oson' yoki 'qiyin' ").lower() 

if choice == 'oson': 
  easy_level()

elif choice == 'qiyin': 
  hard_level()
else: 
  print("Iltimos mos qiymat kiriting")





    







# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.


# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

