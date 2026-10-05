from state import State


class Agent:
    

    def __init__(self, player):
        self.player = player
        # node counter 
        self.minimax_nodes = 0
        self.alphabeta_nodes = 0

    def opponent(self, player):

        if player == "X":
            return "O"

        return "X"
    
    def ab_move(self, state):

        best_score = float("-inf")
        best_move = None
    
        alpha = float("-inf")
        beta = float("inf")
    
        for row, col in state.get_valid_moves():
    
            new_state = state.clone()
            new_state.make_move(row, col, self.player)
    
            score = self.alphabeta(
                new_state,
                self.opponent(self.player),
                alpha,
                beta
            )
    
            if score > best_score:
                best_score = score
                best_move = (row, col)
    
            alpha = max(alpha, best_score)

        return best_move

    def minimax(self, state, current_player):
        # node counter 
        self.minimax_nodes += 1

        # Base case: game over
        if state.is_terminal():
            return state.evaluate(self.player)

        # MAX: AI's turn
        if current_player == self.player:

            best_score = float("-inf")

            for row, col in state.get_valid_moves():

                new_state = state.clone()
                new_state.make_move(row, col, current_player)

                score = self.minimax(
                    new_state,
                    self.opponent(current_player)
                )

                best_score = max(best_score, score)

            return best_score

        # MIN: opponent's turn
        else:

            best_score = float("inf")

            for row, col in state.get_valid_moves():

                new_state = state.clone()
                new_state.make_move(row, col, current_player)

                score = self.minimax(
                    new_state,
                    self.opponent(current_player)
                )

                best_score = min(best_score, score)

            return best_score
        
        
    def alphabeta(self, state, current_player, alpha, beta):
        # node counter 
        self.alphabeta_nodes += 1

        # Base case
        if state.is_terminal():
            return state.evaluate(self.player)

        # MAX
        if current_player == self.player:

            best_score = float("-inf")

            for row, col in state.get_valid_moves():

                new_state = state.clone()
                new_state.make_move(row, col, current_player)
    
                score = self.alphabeta(
                    new_state,
                    self.opponent(current_player),
                    alpha,
                    beta
                )
    
                best_score = max(best_score, score)
    
                # 更新 alpha
                alpha = max(alpha, best_score)
    
                # 剪枝
                if beta <= alpha:
                    break

            return best_score

        # MIN
        else:

            best_score = float("inf")

            for row, col in state.get_valid_moves():

                new_state = state.clone()
                new_state.make_move(row, col, current_player)
    
                score = self.alphabeta(
                    new_state,
                    self.opponent(current_player),
                    alpha,
                    beta
                )

                best_score = min(best_score, score)
    
                # 更新 beta
                beta = min(beta, best_score)
    
                # 剪枝
                if beta <= alpha:
                    break

        return best_score

    def get_move(self, state):

        best_score = float("-inf")
        best_move = None

        for row, col in state.get_valid_moves():

            new_state = state.clone()
            new_state.make_move(row, col, self.player)

            score = self.minimax(
                new_state,
                self.opponent(self.player)
            )

            if score > best_score:
                best_score = score
                best_move = (row, col)

        return best_move
