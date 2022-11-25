from MainGame import MainGame
from Board import Board

def main() -> None:
    current_amount_of_rounds = 0
    game = MainGame()
    board = Board()
    board.show_board(board, current_amount_of_rounds)
    current_amount_of_rounds += 1
    game.play(board, current_amount_of_rounds)
if __name__ == "__main__":
    main()
