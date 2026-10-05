from state import State

# 创建一个空棋盘
board = State(None)

print("初始棋盘：")
print(board)

# 看看哪些位置可以下棋
moves = board.get_valid_moves()
print("可下位置：", moves)
print("空位数量：", len(moves))

# 在中间下一个 X
success = board.make_move(1, 1, "X")

print("落子成功：", success)
print(board)
print("剩余空位：", len(board.get_valid_moves()))
