import random

#This code uses random moves and simple predictions to counter the opponent
# Store their moves history, detect a new move
#Analyze their last 5 moves

def player(prev_play, opponent_history=[]):
    # Store previous moves
    opponent_history.append(prev_play)

    # Default move
    guess = "R"

    # Strategy for Quincy (Detects its 5-move pattern)
    quincy_pattern = ["R", "P", "P", "S", "R"]
    if len(opponent_history) >= 5:
        last_five_moves = opponent_history[-5:]
        if last_five_moves == quincy_pattern:
            guess = "P"  # Always counter the first move "R"

    # Strategy for Kris (Always repeats our last move)
    elif len(opponent_history) > 0 and opponent_history[-1] != "":
        last_move = opponent_history[-1]
        if last_move == "R":
            guess = "P"
        elif last_move == "P":
            guess = "S"
        elif last_move == "S":
            guess = "R"

    # Strategy for Abbey and Mrugesh (Unpredictable play to mislead them)
    else:
        guess = random.choice(["R", "P", "S"])

    return guess
