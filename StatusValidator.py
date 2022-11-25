class StatusValidator:
    def __init__(self):
        pass

    def is_win(self, board, player_symbol):
        pass

    def has_sequence(self, board, player_symbol) -> bool:
        sequence_counter = 0
        for row in board.board:
            for cell in row:
                if sequence_counter == 4:
                    return True

                if player_symbol in cell:
                    sequence_counter += 1
                    print(sequence_counter)
                    continue
                else: 
                    sequence_counter = 0
                    continue
                

        return False    
