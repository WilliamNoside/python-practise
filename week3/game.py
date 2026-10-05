from state import State
from agent import Agent


def play(state, agentA, agentB):

    current_agent = agentA

    while not state.is_terminal():

        print(state)

        move = current_agent.get_move(state)

        row, col = move

        state.make_move(
            row,
            col,
            current_agent.player
        )

        if current_agent == agentA:
            current_agent = agentB
        else:
            current_agent = agentA

    print(state)

    winner = state.get_winner()

    if winner is not None:
        print("Winner:", winner)
        return winner

    print("Draw")
    return None

if __name__ == "__main__":

    state = State(None)

    agentA = Agent("X")
    agentB = Agent("O")

    play(state, agentA, agentB)