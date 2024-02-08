def print_board(board):
    for row in board:
        print(" | ".join(str(cell).rjust(2) for cell in row))
        print("-" * 25)


def check_bingo(board):
    # 横方向のビンゴをチェック
    for row in board:
        if all(cell == 'X' for cell in row):
            return True

    # 縦方向のビンゴをチェック
    for col in range(5):
        if all(board[row][col] == 'X' for row in range(5)):
            return True

    # 対角線のビンゴをチェック
    if all(board[i][i] == 'X' for i in range(5)) or all(board[i][4 - i] == 'X' for i in range(5)):
        return True

    return False


def mark_number(board, number):
    for row in range(5):
        for col in range(5):
            if board[row][col] == number:
                board[row][col] = 'X'


b1 = [
    [24, 45, 65, 68, 57],
    [79, 4, 59, 94, 54],
    [80, 64, 48, 96, 75],
    [67, 78, 36, 23, 16],
    [84, 62, 91, 31, 61],
]
b2 = [
    [39, 82, 68, 10, 99],
    [96, 38, 56, 27, 47],
    [25, 60, 73, 93, 22],
    [19, 26, 49, 71, 23],
    [28, 65, 32, 58, 63],
]
b3 = [
    [6, 59, 54, 86, 77],
    [84, 60, 28, 61, 79],
    [74, 91, 20, 11, 51],
    [18, 29, 2, 33, 94],
    [45, 30, 55, 90, 36],
]
b4 = [
    [8, 4, 70, 57, 95],
    [54, 80, 69, 94, 45],
    [61, 33, 92, 28, 36],
    [55, 79, 32, 84, 60],
    [88, 83, 99, 27, 20],
]

hands = [24, 37, 60, 45, 51, 58, 78, 38, 66, 61, 79, 83, 26, 40, 16, 43, 39, 50, 29, 75, 54, 15, 7, 36, 98, 56, 3, 53,
         34,
         87, 49, 88, 90, 31, 42, 4, 65, 35, 91, 74, 47, 21, 1, 97, 73, 72, 99, 11, 55, 84]

# 各ビンゴボードを手札でマークする
for hand in hands:
    mark_number(b1, hand)
    mark_number(b2, hand)
    mark_number(b3, hand)
    mark_number(b4, hand)

# すべての手札を使用した後にビンゴが達成されていないかチェック
if not any(check_bingo(board) for board in [b1, b2, b3, b4]):
    print("No Bingo!")
    