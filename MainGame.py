from Player import Player

class MainGame:
    def __init__(self):
        self.player_one = Player(self.get_user_name(1), self.get_user_symbol(1))
        self.player_two = Player(self.get_user_name(2), self.get_user_symbol(2))

    def get_user_name(self, player_count) -> str:
        new_player_name = input(f"Player {player_count}: Please enter your name: ")

        return new_player_name

    def get_user_symbol(self, player_count) -> str:
        while True:
            try:
                new_player_symbol = input(
                    f"Player {player_count}: Please enter your wanted symbol, you can chose between O and X: "
                )
                if new_player_symbol == "X" or new_player_symbol == "O":
                    return new_player_symbol
                else:
                    raise ValueError

            except ValueError:
                print("Please enter X or O for your symbol.")

    def turn(self, player_name, player_symbol, board) -> None:
        while True:
            try:
                column_number = self.get_column_input(player_name)
                if board.is_valid_turn(column_number):
                    break
                else:
                    raise ValueError

            except ValueError:
                print(f"You can't put a coin in column {column_number + 1}")
                continue

        board.add_coin_to_board(column_number, player_symbol)

        return

    def get_column_input(self, player_name) -> int:
        return int(input(f"{player_name}: Select a row to put your coin: ")) - 1
        
    def round(self, board, current_amount_of_rounds, status_validator) -> None:
        self.turn(self.player_one.name, self.player_one.symbol, board)

        board.show_board(current_amount_of_rounds)
        self.turn(self.player_two.name, self.player_two.symbol, board)
        board.show_board(current_amount_of_rounds)


        self.turn(self.player_two.name, self.player_two.symbol, board)
        print(status_validator.has_sequence(board, self.player_two.symbol))

        board.show_board(board, current_amount_of_rounds)
        


    def play(self, board, current_amount_of_rounds, status_validator) -> None:
        while True:
            self.round(board, current_amount_of_rounds, status_validator), status_validator
            current_amount_of_rounds += 1
