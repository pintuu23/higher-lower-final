from game_data import data
import random
from art import logo, vs

def random_account():
    return random.choice(data)

def format_data(account):
    name= account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name},a {description}, from {country}"
def answer_checking(guess, a_folllowers, b_followers):
    if a_folllowers>b_followers:
        return guess=="a"
    else:
        return guess=="b"
def game():
    score=0
    game_continue=True
    account_a=random_account()
    account_b= random_account()

    while game_continue:
        account_a = account_b
        account_b=random_account()

        while account_a==account_b:
            account_b=random_account()
        print(f"compare A : {format_data(account_a)}.")
        print(vs)
        print(f"compare A : {format_data(account_b)}.")

        guess= input("Who has more followers ? A or B").lower()
        a_follower=account_a["follower_count"]
        b_follower=account_b["follower_count"]
        is_correct= answer_checking(guess, a_follower,b_follower)

        if is_correct:
            score+=1
            print(f"You're right! Current score : {score}.")
        else:
            game_continue=False
            print(f" Sorry , that's wrong. Final score : {score}")
game()



# print(random_account())
