class StatusValidator:
    @staticmethod
    def is_horizontal_win(board, player_symbol) -> bool:
        for row in board.board:
            sequence_counter = 0
            for cell in row:
                if sequence_counter == 4:
                    return True

                if player_symbol in cell:
                    sequence_counter += 1
                else: 
                    sequence_counter = 0

        return False

    @staticmethod
    def is_vertical_win(board, player_symbol) -> bool:
        sequence_counter = 0
        for cell_index_in_row in range(5):
            for row in board.board:
                if sequence_counter == 4:
                    return True

                if player_symbol in row[cell_index_in_row]:
                    sequence_counter += 1
                else:
                    sequence_counter = 0

        return False

    @staticmethod
    def is_diagonal_win(board, player_symbol) -> bool:
        sequence_counter = 0
        for cell_index_in_row in range(2):
            for row in board.board:
                old_cell_index_in_row = cell_index_in_row
                if sequence_counter == 4:
                    return True

                player_symbol_is_in_current_cell = player_symbol in row[cell_index_in_row]
                if player_symbol_is_in_current_cell:
                    sequence_counter += 1
                    cell_index_in_row += 1
                else:
                    sequence_counter = 0
                    cell_index_in_row = old_cell_index_in_row

        sequence_counter = 0
        for cell_index_in_row in range(5, 3, -1):
            for row in board.board:
                old_cell_index_in_row = cell_index_in_row
                if sequence_counter == 4:
                    return True

                player_symbol_is_in_current_cell = player_symbol in row[cell_index_in_row]
                if player_symbol_is_in_current_cell:
                    sequence_counter += 1
                    cell_index_in_row -= 1
                else:
                    sequence_counter = 0
                    cell_index_in_row = old_cell_index_in_row

        return False

    @staticmethod
    def board_is_full(board) -> bool:
        for cell in board.board[0]:
            if '_' in cell:
                return False

        return True

    @staticmethod
    def is_win(board, player_symbol) -> bool:
        return StatusValidator.is_horizontal_win(board, player_symbol) or StatusValidator.is_vertical_win(board, player_symbol) or StatusValidator.is_diagonal_win(board, player_symbol)
