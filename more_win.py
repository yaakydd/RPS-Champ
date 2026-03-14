import random

# This code uses pattern recognition to adjust our moves to make us get more than 60% wins

def player(previous_play, opponent_history=[]):
    # Keep track of opponent's history
    if previous_play:
        opponent_history.append(previous_play)

    # Default move
    guess = "R"
    
    # If we have enough history, use pattern recognition
    if len(opponent_history) > 5:
        # Find the most common previous move of opponent
        last_moves = "".join(opponent_history[-5:])  # Get last 5 moves
        common_move = max(set(opponent_history), key=opponent_history.count)  # Most frequent move
        
        # Counter the most frequent move
        counter_moves = {"R": "P", "P": "S", "S": "R"}
        guess = counter_moves[common_move]

    return guess
