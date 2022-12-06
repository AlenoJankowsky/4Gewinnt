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
    while True:
        game.play(board, current_amount_of_rounds, status_validator)
        while True:
            try:
                play_again = input("Do you want to play again? Y/N? ").upper()
                if play_again == 'Y':
                    current_amount_of_rounds = 0
                    board = Board()
                    status_validator = StatusValidator()
                    board.show_board(current_amount_of_rounds)
                    current_amount_of_rounds += 1
                    break
                elif play_again == 'N':
                    return
                else:
                    raise ValueError
            except ValueError:
                print("Please enter Y or N. ", end="")
        
if __name__ == "__main__":
    main()
