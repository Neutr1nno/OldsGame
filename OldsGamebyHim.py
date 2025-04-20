def generate_empty_game_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def render_game_board(game_board):
    for board_row in game_board:
        print(" | ".join(board_row))
        print("-" * 9)

def check_winner(board, player):
   
    for row in board:
        if all(cell == player for cell in row):
            return True
  
    for column_index in range(3):
        if all(board[row_index][column_index] == player for row_index in range(3)):
            return True
   
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_draw(board):
    return all(cell != " " for row in board for cell in row)

def oldsGame():
    board = generate_empty_game_board()
    current_player = "X"

    while True:
        render_game_board(board)
        print(f"Vez do jogador {current_player}")
        
        try:
            board_row = int(input("Escolha a linha (0, 1, 2): "))
            board_column = int(input("Escolha a coluna (0, 1, 2): "))
        except ValueError:
            print("Por favor, digite números válidos.")
            continue

        if board_row not in [0, 1, 2] or board_column not in [0, 1, 2]:
            print("Posição inválida! Tente novamente.")
            continue

        if board[board_row][board_column] != " ":
            print("Essa posição já está ocupada! Tente outra.")
            continue

        board[board_row][board_column] = current_player

        if check_winner(board, current_player):
            render_game_board(board)
            print(f"Jogador {current_player} venceu! 🎉")
            break

        if check_draw(board):
            render_game_board(board)
            print("Empate! 🤝")
            break

        current_player = "O" if current_player == "X" else "X"


oldsGame()