from logo import logo, vs
from game_data import data
import random

SCORE = 0

def game():
    print("Welcome to the comparing game!")
    print(logo)
    a = random.choice(data)
    b = random.choice(data)
    
    while a == b:
        b = random.choice(data)
    
    score_checker(a, b)

def score_checker(first, second):
    global SCORE

    if first["follower_count"] > second["follower_count"]:
        right_answer = "A"
        for_new = first
    else:
        right_answer = "B"
        for_new = second

    print(f"Compare A: {first['name']}, {first['description']}")
    print(vs)
    print(f"Against B: {second['name']}, {second['description']}")
    user_answer = input("Who has more followers? Type 'A' or 'B' ").upper()

    if user_answer != right_answer:
        print("Unfortunately, you are not right")
        print(f"Your score is {SCORE}")
        return 

    SCORE += 1
    new_data = random.choice(data)
    while new_data == first or new_data == second:
        new_data = random.choice(data)
    data.remove(new_data)
    score_checker(for_new, new_data)

game()