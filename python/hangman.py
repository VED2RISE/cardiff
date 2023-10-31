import random
from hangman_words import word_list
from hangman_logo import logo

print("WELLCOME TO THE HANGMAN GAME!")
print(logo)

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


chosen_word = random.choice(word_list)

used = []
used1 = []
display = []

for _ in chosen_word:
    display.append(" _ ")

end_of_the_game = False
lives = 6

while not end_of_the_game:

    if lives <=0:
        end_of_the_game = True
        print("\nUnfortunately you've lost")
        print(f"\nThe word was {chosen_word}")

    guess = input("\nGuess a letter: ").lower()
    found = False
    
    if guess in used1:
        print("\nYou've already used that letter try another")
    

    for j in range(len(chosen_word)):
        if chosen_word[j] == guess:
            display[j] = guess
            found = True
            used1.append(guess)

    if not found and guess in used:
        print("\nYou already used that letter, try another")
    
    if not found and guess not in used:
        print("\nWrong!")
        print(stages[lives-1])
        lives -= 1
        used.append(guess)
        
    for n in display:
        print(f"{n} ", end = "")

    if " _ " not in display:
        end_of_game = True
        print("\nCongrats! You've won!")