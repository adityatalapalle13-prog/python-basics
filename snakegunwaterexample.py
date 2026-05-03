import random

words=("snake","water","gun")

repeat=True

while repeat:
    inp = input("choose snake or gun or water or exit: ")

    if inp.casefold() == "exit":
        repeat = False

    word=random.choice(words)

    if inp.casefold()=="snake" and word=="snake":
        print("tie")


    elif inp.casefold()=="snake" and word=="water":
        print("you win")

    elif inp.casefold()=="snake" and word=="gun":
        print("system wins")


    elif inp.casefold()=="gun" and word=="snake":
        print("you win")

    elif inp.casefold()=="gun" and word=="gun":
        print("tie")

    elif inp.casefold()=="gun" and word=="water":
        print("system wins")

    elif inp.casefold()=="water" and word=="snake":
        print("system wins")

    elif inp.casefold()=="water" and word=="water":
        print("tie")

    elif inp.casefold()=="water" and word=="gun":
        print("you win")

    else:
        print("incorrect input")
