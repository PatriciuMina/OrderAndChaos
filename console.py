import random
from service import Service
from board import Board
class Console:
    def __init__(self, service):
        self.service = service
    def print_board(self):
        print("BOARD")
        board = self.service.get_board()
        for line in board:
            print(line)
        print("")


    def run(self):

        game= True
        turn= True
        while game == True:
            row = 0
            collum = 0
            symbol = 'x'
            self.service.computer_move(row, collum, symbol)
            if self.service.check_end_order() == True:
                game= False
                self.print_board()
                print("Order Won the game")
                break
            if self.service.check_end_chaos() == True:
                game = False
                self.print_board()
                print("Chaos Won the game")
                break

            self.print_board()
            cmd = input("Enter the row, collum and symbol")
            cmd = cmd.split()

            try:
                row= int(cmd[0])
                if (row != int(row)):
                    raise Exception
                collum = int(cmd[1])
                if (collum!= int(collum)):
                    raise Exception
                symbol = cmd[2]
                self.service.player_move(row, collum, symbol)
            except Exception:
                print("Invalid move")

            if self.service.check_end_order() == True:
                game= False
                self.print_board()
                print("Order Won the game")
            if self.service.check_end_chaos() == True:
                game = False
                self.print_board()
                print("Chaos Won the game")

















