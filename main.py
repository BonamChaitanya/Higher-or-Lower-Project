# display art
from art import logo, vs
from game_data import data
import random


def format_data(account):
    """Takes the account data and returns the printable format"""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"


def check_answer(user_guess, a_followers, b_followers):
    """Take a user's guess and the followers counts and returns if they got it right."""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"



print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    # generate a random account from the game data
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    #ask users for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    print("\n" * 10)
    print(logo)

    #check if user is correct
    #get follower count of each account
    a_follower_account = account_a["follower_count"]
    b_follower_account = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_account, b_follower_account)

    #use iff statement to check if user is correct

    # give user feedback on their guess
    if is_correct:
        score += 1
        print(f"You're right! Current Score: {score}")
    else:
        print(f"Sorry that's wrong! Final Score: {score}")
        game_should_continue = False



# score keeping

# make the game repeatable

# making the account at position B becomes the next account at position A

