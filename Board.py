class Board:  
    def __init__(self):
        self.board = Board.create_board(self)

    def create_board(self) -> list[list[str]]:
        new_board = [['|_|''_|''_|''_|''_|''_|'],
                     ['|_|''_|''_|''_|''_|''_|'],
                     ['|_|''_|''_|''_|''_|''_|'],
                     ['|_|''_|''_|''_|''_|''_|'],
                     ['|_|''_|''_|''_|''_|''_|'],
                     ['|_|''_|''_|''_|''_|''_|'],
                     ['|1|''2|''3|''4|''5|''6|']]
        
        return new_board

    def show_board(self, board, current_amount_of_rounds) -> None:
        print("Round: " + str(current_amount_of_rounds))
        for row in board:
            for cell in row:
                print(cell)

        print("\n")
        