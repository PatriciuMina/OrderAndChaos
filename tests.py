
from board import Board
import unittest


class Test(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

    def test_chaos_win(self):
        self.board = Board()
        board = self.board.game_board()
        board[1][1]='x'
        board[1][2]='x'
        board[1][3]='x'
        board[1][4]='x'
        board[1][5]='x'
        winner = self.board.check_order_win()
        self.assertEqual(winner, True)
    def test_order_win(self):
        self.board= Board()
        board =self.board.game_board()
        board[0][1] = '0'
        board[1][2] = 'x'
        board[1][3] = 'x'
        board[1][4] = 'x'
        board[1][5] = 'x'
        winner = self.board.check_chaos_win()
        self.assertEqual(winner,False)
    def test_order_win(self):
        self.board= Board()
        board =self.board.game_board()
        board[0][1] = '0'
        board[1][2] = 'x'
        board[1][3] = 'x'
        board[1][4] = 'x'
        board[1][5] = 'x'
        winner = self.board.check_chaos_win()
        self.assertEqual(winner,False)
    def test_chaos_win(self):
        self.board = Board()
        board = self.board.game_board()
        board[1][1]='x'
        board[1][2]='x'
        board[1][3]='x'
        board[1][4]='x'
        board[1][5]='x'
        winner = self.board.check_order_win()
        self.assertEqual(winner, True)

