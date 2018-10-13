#!/usr/bin/python3

import random
from enum import Enum

class Hand(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2

class Outcomes(Enum):
    WIN = 0
    DRAW = 1
    LOSE = 2

class WinGraph:
    win_dict = {Hand.ROCK :     {Hand.ROCK : Outcomes.DRAW
                                 Hand.PAPER : Outcomes.LOSE                    
                                 Hand.SCISSORS : Outcomes.WIN}
                Hand.PAPER :    {Hand.ROCK : Outcomes.WIN
                                 Hand.PAPER : Outcomes.DRAW                    
                                 Hand.SCISSORS : Outcomes.LOSE}
                Hand.SCISSORS : {Hand.ROCK : Outcomes.LOSE
                                 Hand.PAPER : Outcomes.WIN                 
                                 Hand.SCISSORS : Outcomes.DRAW}}
    
    def outcome(player_hand, cpu_hand):
        return win_dict[player_hand][cpu_hand]

if __name__ == "__main__":
    print("Welcome to ROCK PAPER SCISSORS")
    while (True):
        player_choice = 0;
        input_choice = {"r": Hand.ROCK, "p": Hand.PAPER, "s": Hand.SCISSORS}
        while (True):
            choice = input("Please select a hand; R/P/S")
            
            if (typeof(choice) is str) and (choice in input_choice.keys()):
                player_choice = input_choice[choice.lower()]
                break
            else:
                print("Please input a valid option")
       
       cpu_choice = random.choice([Hand.ROCK, Hand.PAPER, Hand.SCISSORS])

       outcome = Outcone.outcome(player_choice, cpu_choice)
       if outcome == Outcome.WIN:
           print("You are the champian of all gods")
       elif outcome == Outcome.DRAW:
           print("Huh, that's one's a draw then")
       elif outcome == Outcome.LOSE:
           print("Ha ha, you lose")

