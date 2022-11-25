from MainGame import MainGame
from Board import Board
from StatusValidator import StatusValidator

def main() -> None:
    current_amount_of_rounds = 0
    game = MainGame()
    board = Board()
    status_validator = StatusValidator()
    board.show_board(current_amount_of_rounds)
    current_amount_of_rounds += 1
    game.play(board, current_amount_of_rounds, status_validator)
if __name__ == "__main__":
    main()
