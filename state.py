class State:
    size = 3  # Size of the Tic-Tac-Toe grid (3x3)

    def __init__(self, grid):
        '''
        param: grid - list of lists (a 3x3 matrix representing the board)
        If grid is None, initialize an empty board.
        '''
        if grid is None:
            self.grid = [[' ' for _ in range(State.size)] for _ in range(State.size)]
        else:
            assert(len(grid) == State.size)
            assert(len(grid[0]) == State.size)
            self.grid = [row[:] for row in grid]  # Deep copy to avoid mutation

    def __str__(self):
        '''Return a string representation of the board.'''
        out = ''
        for row in self.grid:
            out += '|'.join(row) + '\n'
            out += '-' * 5 + '\n'
        return out

    def get_valid_moves(self):
        '''Return a list of (row, col) tuples for empty cells.'''
        moves = []
        for r in range(State.size):
            for c in range(State.size):
                if self.grid[r][c] == ' ':
                    moves.append((r, c))
        return moves

    def get_winner(self):
        '''Return 'X', 'O', or None depending on the game state.'''
        lines = []

        # Rows and columns
        for i in range(State.size):
            lines.append(self.grid[i])  # Row
            lines.append([self.grid[r][i] for r in range(State.size)])  # Column

        # Diagonals
        lines.append([self.grid[i][i] for i in range(State.size)])
        lines.append([self.grid[i][State.size - 1 - i] for i in range(State.size)])

        for line in lines:
            if line[0] != ' ' and line.count(line[0]) == State.size:
                return line[0]
        return None

    def is_terminal(self):
        '''Check if the game is over (win or draw).'''
        return self.get_winner() is not None or not self.get_valid_moves()

    def evaluate(self, player):
        '''
        Return +1 if player wins, -1 if player loses, 0 otherwise.
        Used for AI evaluation.
        '''
        winner = self.get_winner()
        if winner == player:
            return 1
        elif winner is None:
            return 0
        return -1

    def make_move(self, row, col, player):
        '''
        Apply a move for the given player.
        Return True if successful, False if the cell is occupied.
        '''
        assert player in ['X', 'O']
        if self.grid[row][col] == ' ':
            self.grid[row][col] = player
            return True
        return False

    def undo_move(self, row, col):
        '''Undo a move (used in backtracking for AI).'''
        if self.grid[row][col] != ' ':
            self.grid[row][col] = ' '

    def clone(self):
        '''Return a deep copy of the game state (for simulation).'''
        new_state = State(None)
        new_state.grid = [row[:] for row in self.grid]
        return new_state