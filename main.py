import pyjokes
import random
from prettytable import from_csv
from art import *


def guessing_numbers():
    """
    Це гра "Вгадай число". В ній у вас е безкінечні спроби вгадати число.
    :return:
    """
    num = random.randrange(1, 100)
    print("Guess the number 1 - 100\nYou have endless attempts: ")
    while True:
        you_choice = int(input("#>"))
        if you_choice == num:
            print("You Win")
            break
        elif you_choice < num:
            print("Your number is to low!")
        elif you_choice > num:
            print("Your number is too high!")


def preattytable_move():
    """
    Це балиця з найпопулярнішими фільмами. Цю таблицю можна розширити за допомогою редагування файлу csv.
    Цей файл знаходиться у папці files.
    :return:
    """
    with open("files/move_file.csv") as fp:
        mytable = from_csv(fp)
    return mytable


choice = 0
tprint("Make a choice!", font="small", chr_ignore=True)
while True:
    """
    Це головне меню бота. Тут ві вибираїте що саме вам потрібно.
    :return:
    """
    print("(1)Jokes, (2)Recommended movies, (3)Play the game")

    choice = input("#> ")
    if choice == "1":
        tprint("Joke", font="small", chr_ignore=True)
        print("'" + pyjokes.get_joke() + "'")
    elif choice == "2":
        tprint("Recommended movies", font="small", chr_ignore=True)
        print(preattytable_move())
    elif choice == "3":
        tprint("Guess the number", font="small", chr_ignore=True)
        guessing_numbers()
    elif choice == "end":
        break
    else:
        continue
