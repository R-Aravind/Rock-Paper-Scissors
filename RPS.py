# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

import random

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    # guess = "R"

    guesses = ["R", "P", "S"]
    guess = random.choice(guesses) 

    defeated_by = { "R" : "P",
                    "P" : "S",
                    "S" : "R", 
                    "" : guess }

    defeats = { "P" : "R",
                "R" : "S",
                "S" : "P", 
                "" : guess }

    if len(opponent_history):
      guess = defeated_by[prev_play]

    # if len(opponent_history) > 2:
    #   if defeated_by[prev_play] == defeats[opponent_history[-2]]:
    #     guess = opponent_history[-2]

    return guess
