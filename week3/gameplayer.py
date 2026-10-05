from state import State
from agent import Agent


def play(state, agentA, agentB):

    current_player = "X"

    while not state.is_terminal():

        print(state)

        # Decide whose turn it is
        if current_player == "X":
            current_agent = agentA
        else:
            current_agent = agentB

        # Human player
        if current_agent is None:

            print("Your turn:", current_player)

            row = int(input("Row (0-2): "))
            col = int(input("Col (0-2): "))

            # Check valid position
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid position!")
                continue

            # Check occupied cell
            if not state.make_move(row, col, current_player):
                print("That cell is already occupied!")
                continue

        # AI player
        else:

            move = current_agent.get_move(state)

            row, col = move

            print("AI chooses:", move)

            state.make_move(
                row,
                col,
                current_player
            )

        # Switch player
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

    # Final board
    print(state)

    winner = state.get_winner()

    if winner is not None:
        print("Winner:", winner)
        return winner

    print("Draw")
    return None

if __name__ == "__main__":

    state = State(None)

    # Human = X
    agentA = None

    # AI = O
    agentB = Agent("O")

    play(state, agentA, agentB)