from state import State
from agent import Agent


board = State([
    ["X", " ", "O"],
    ["O", " ", " "],
    [" ", " ", " "]
])

print(board)

ai = Agent("X")


# --------------------
# Minimax
# --------------------

ai.minimax_nodes = 0

move = ai.get_move(board)

print("Minimax move:", move)
print("Minimax searched nodes:", ai.minimax_nodes)


# --------------------
# Alpha-Beta
# --------------------

ai.alphabeta_nodes = 0

move2 = ai.ab_move(board)

print("Alpha-Beta move:", move2)
print("Alpha-Beta searched nodes:", ai.alphabeta_nodes)