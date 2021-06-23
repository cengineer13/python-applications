#Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.

display = [] 
#For each letter in the chosen_word, add a "_" to 'display'.
for _ in chosen_word:
  display+="_"

print(display)
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

guess = input("Guess a letter: ").lower()

#TODO-2: - Loop through each position in the chosen_word;

for position in range(len(chosen_word)):
  letter = chosen_word[position]
  
  if letter == guess:
    display[position] = letter 
  
  

print(display)

