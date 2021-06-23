#HINT: You can call clear() to clear the output in the console.


auction = {}

cycle = True 

def winner(auction): 
  max_bid = 0 
  for name in auction: 
    bid = auction[name] 
  
    if bid > max_bid:
      max_bid = bid
      winner_name = name  
  print(f"{winner_name} won the bid with {max_bid}$")


while cycle:
  name = input("What is your name? ").lower() 
  bid = int(input("What is your bid? $"))
  
  auction[name] = bid 
  
  any_person = input("Is there any person to continue auction? yes/no ").lower() 

  if any_person == "yes":
    pass
  else: 
    cycle = False  

winner(auction)

   








