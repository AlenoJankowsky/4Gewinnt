class Board:
    def __init__(self):
        self.board = self.create_board()

    def create_board(self) -> list[list[str]]:
        new_board = [['|_|','_|','_|','_|','_|','_|'],
                     ['|_|','_|','_|','_|','_|','_|'],
                     ['|_|','_|','_|','_|','_|','_|'],
                     ['|_|','_|','_|','_|','_|','_|'],
                     ['|_|','_|','_|','_|','_|','_|'],
                     ['|_|','_|','_|','_|','_|','_|'],
                     ['|1|''2|''3|''4|''5|''6|']]

        return new_board

    def show_board(self, current_amount_of_rounds) -> None:
        cell_counter = 0
        print("Round: " + str(current_amount_of_rounds))
        for row in self.board:
            cell_counter = 0
            for cell in row:
                if cell_counter == 5:
                    print(cell)
                    continue
                else:
                    print(cell, end="")

                cell_counter += 1

        print("\n")

    def is_valid_turn(self, column_number) -> bool:
        user_input_is_not_in_range = column_number > 5 or column_number < 0
        if user_input_is_not_in_range:
            return False

        first_cell_in_column_is_free = '_' in self.board[0][column_number]
        if not first_cell_in_column_is_free:
            return False
        else:
            return True

    def add_coin_to_board(self, column_number, player_symbol) -> None:
        board_iterator = -2
        next_valid_cell_is_found = False
        while not next_valid_cell_is_found or board_iterator == -6:
            if '_' in self.board[board_iterator][column_number]:
                self.board[board_iterator][column_number] = self.board[board_iterator][column_number].replace('_', player_symbol)
                next_valid_cell_is_found = True

                return
            else:
                board_iterator -= 1
