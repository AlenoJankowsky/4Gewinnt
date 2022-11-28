class StatusValidator:
    def __init__(self):
        pass

    def is_win(self, board, player_symbol) -> bool:
        if self.is_horizontal_win(board, player_symbol) or self.is_vertical_win(board, player_symbol):
            return True

    def is_horizontal_win(self, board, player_symbol) -> bool:
        sequence_counter = 0
        for row in board.board:
            for cell in row:
                if sequence_counter == 4:
                    return True

                if player_symbol in cell:
                    sequence_counter += 1
                    continue
                else: 
                    sequence_counter = 0

        return False

    def is_vertical_win(self, board, player_symbol) -> bool:
        sequence_counter = 0
        cell_index_in_row = 0

        for row in board.board:
            if sequence_counter == 4:
                return True
            
            if player_symbol in row[cell_index_in_row]:
                sequence_counter += 1
                continue
            else:
                sequence_counter = 0


        return False

    def is_diagonal_win(self, board, player_symbol) -> bool:
        sequence_counter = 0
        cell_index_in_row_from_left = 0
        cell_index_in_row_from_right = 5
        for row in board.board:
            if sequence_counter == 4:
                return True
            
            if player_symbol in row[cell_index_in_row_from_left]:
                sequence_counter += 1
                cell_index_in_row_from_left += 1
                print(sequence_counter)
                continue
            else:
                sequence_counter = 0

        for row in board.board:
            if sequence_counter == 4:
                return True

            if player_symbol in row[cell_index_in_row_from_right]:
                sequence_counter += 1
                cell_index_in_row_from_right -= 1
                continue
            else:
                sequence_counter = 0

        return False
        