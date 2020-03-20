from board import Board
class Service:
    def __init__(self,board):
        self.board =board
    def get_board(self):
        return self.board.get_game_board()

    def player_move(self, player_row, player_collum, symbol):
        self.board.move_player(player_row, player_collum,symbol)

    def computer_move(self, row, collum,symbol):
        self.board.move_computer(row, collum,symbol)


    def check_end_order(self):
        return self.board.check_order_win()

    def check_end_chaos(self):
        return self.board.check_chaos_win()

