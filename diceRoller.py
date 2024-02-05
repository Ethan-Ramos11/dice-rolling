import questionary
import random
from termcolor import colored


def getNumDice():
    return questionary.select(
        "How many dice do you want roll?",
        choices=["1", "2", "3", "4", "5", "6", "7"]
    ).ask()


def getNumSides():
    pass


def printRolls(rolls):
    pass


def diceSimulator():
    pass
