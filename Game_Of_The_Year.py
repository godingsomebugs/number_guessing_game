# build 1.1

import os
import random
import time

def clearTerminal():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def printC(text, color):
    if color == None:
        print(text)
    if color == "red":
        print("\033[91m"+text+"\033[0m")
    if color == "green":
        print("\033[92m"+text+"\033[0m")
    if color == "yellow":
        print("\033[93m"+text+"\033[0m")
    if color == "blue":
        print("\033[94m"+text+"\033[0m")

def game(diff):
    clearTerminal()

    if diff == 1:
        diffDesc = "Very Easy(1-3)"
        number = random.randint(1,3)
    if diff == 2:
        diffDesc = "Easy(1-5)"
        number = random.randint(1,5)
    if diff == 3:
        diffDesc = "Standart(1-10)"
        number = random.randint(1,10)
    if diff == 4:
        diffDesc = "Hard(1-20)"
        number = random.randint(1,20)
    if diff == 5:
        diffDesc = "Very Hard(1-50)"
        number = random.randint(1,50)

    print("Guess a number! "+diffDesc)
    guessRaw = input()

    if guessRaw == "":
        printC("Enter a number!", "blue")
        time.sleep(1)
        game(diff)
    if int(guessRaw) == number:
        printC("You win!", "green")
        time.sleep(1)
        game(diff)
    else:
        printC("Wrong!", "red")
        time.sleep(0.5)
        printC("Deleting: C:/windows/system32", "yellow")

        time.sleep(1)

        print("Just kidding!")

        time.sleep(1)
        game(diff)

clearTerminal()
printC("Number Guessing Game 1.0", "blue")
inputRaw = input("difficulty(1-5): ")

if inputRaw == "":
    game(3)
else:
    difficulty = int(inputRaw)
    game(difficulty)