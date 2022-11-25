class Board:
    def __init__(self):
        self.board = Board.create_board(self)

    def create_board(self) -> list[list[str]]:
        new_board = [['|_|','_|','_|','_|','_|','_|'],
                     ['|_|','_|','_|','_|','_|','_|'],
                     ['|_|','_|','_|','_|','_|','_|'],
                     ['|_|','_|','_|','_|','_|','_|'],
                     ['|_|','_|','_|','_|','_|','_|'],
                     ['|_|','_|','_|','_|','_|','_|'],
                     ['|1|''2|''3|''4|''5|''6|']]

        return new_board

    def show_board(self, board, current_amount_of_rounds) -> None:
        cell_counter = 0
        print("Round: " + str(current_amount_of_rounds))
        for row in board.board:
            cell_counter = 0
            for cell in row:
                if cell_counter == 5:
                    print(cell)
                    continue
                else:
                    print(cell, end="")

                cell_counter += 1

        print("\n")

    def is_valid_turn(self, board, column_number) -> bool:
        if column_number > 6 or column_number < 0:
            return False
        elif not '_' in board.board[0][column_number]:
            return False
        else:
            return True

    def add_coin_to_board(self, board, column_number, player_symbol) -> None:
        board_iterator = -2
        next_valid_cell_is_found = False
        while not next_valid_cell_is_found or board_iterator == -6:
            if '_' in board.board[board_iterator][column_number]:
                board.board[board_iterator][column_number] = board.board[board_iterator][column_number].replace('_', player_symbol)
                next_valid_cell_is_found = True

                return
            else:
                board_iterator -= 1
                continue
