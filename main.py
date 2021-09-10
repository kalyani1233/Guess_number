
from random import randint
from colorama import *
from art import *
Easy_Level = 10
Hard_Level = 5
turns = 0


def set_difficulty():
    try:
        level = input("Choose any difficulty level ->hard/easy")
    except:

        print(Fore.BLUE,"Enter easy/hard:")
    finally:
        if level == 'easy':
            global turns
            turns = Easy_Level
            return turns
        else:

            turns =Hard_Level
            return  turns



def check_answer(guess,answer,turns):
    if guess>answer:
        print(Fore.RED,"Too High!!😜😜 ")#5 4 3 2 1
        return turns-1

    elif guess<answer:
        print(Fore.RED,"Too Low!! ")
        return  turns - 1
    else:
        print(Fore.GREEN,"You got it!!the answer is", answer)


def game():
    print(Fore.YELLOW,"welcome to guessing game!!!")
    print(Fore.YELLOW,"I am thinking a no between 1 to 100...")
    answer = randint(1 , 100) # randomly one no get selected
    turns = set_difficulty()
    guess=0
    while guess!=answer:

        print(Fore.RED,f"You have {turns} attempts to print")
        guess= int(input("Make a guess:"))
        turns= check_answer(guess,answer,turns)

        if turns == 0:
            print(Fore.YELLOW,"You have run out of guesses,you lose!!!")
            break
        elif guess!=answer:
            print(Fore.GREEN,"guess again")


game()