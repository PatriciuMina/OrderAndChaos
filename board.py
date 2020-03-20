import random
class Board:
    def __init__(self):
        self.game_board= [['-']*6,['-']*6,['-']*6,['-']*6,['-']*6,['-']*6]

    def get_game_board(self):
        return self.game_board

    def move_player(self, row, collum, symbol ):
        board = self.game_board
        try:
            if board[row][collum]== 'o' or board[row][collum]== 'x':
                 raise Exception("Invalid move")
            if row>5 or collum>5 or row<0 or collum<0:
                raise Exception("Invalid move")

            if board[row][collum] == '-':
                board[row][collum] = symbol
        except Exception:
            print("Invalid move")

    def move_computer(self, row, collum, symbol):
        x = True
        while (x == True):
            position_row = [0, 1, 2, 3, 4, 5]
            position_collum = [0, 1, 2, 3, 4, 5]
            board = self.game_board
            for i in range(6):
                if board[i][0] == board[i][1] == board[i][2] == board[i][3] == 'x':
                    if board[i][4] == "-":
                        board[i][4] = 'x'
                        x = False
                        break
                if board[i][5] == board[i][4] == board[i][2] == board[i][3] == 'x':
                    if board[i][1] == "-":
                        board[i][1] = 'x'
                        x = False
                        break
                if board[i][1] == board[i][2] == board[i][3] == board[i][4] == 'x':
                    if board[i][5] == "-":
                        board[i][5] = 'x'
                        x = False
                        break
                    elif board[i][0] == "-":
                        board[i][0] = 'x'
                        x = False
                        break
                if board[0][i] == board[1][i] == board[2][i] == board[3][i] == 'x':
                    if board[4][i] == "-":
                        board[4][i] = 'x'
                        x = False
                        break
                if board[5][i] == board[4][i] == board[2][i] == board[3][i] == 'x':
                    if board[1][i] == "-":
                        board[1][i] = 'x'
                        x = False
                        break
                if board[1][i] == board[2][i] == board[3][i] == board[4][i] == 'x':
                    if board[5][i] == "-":
                        board[5][i] = 'x'
                        x = False
                        break
                    elif board[0][i] == "-":
                        board[0][i] = 'x'
                        x = False
                        break
                    
            if board[0][0] == board[1][1] == board[2][2] == board[3][3] == 'x':
                if board[4][4] == "-":
                    board[4][4] = 'x'
                    x = False
                    break
            if board[5][5] == board[4][4] == board[2][2] == board[3][3] == 'x':
                if board[1][1] == "-":
                    board[1][1] = 'x'
                    x = False
                    break
            if board[1][1] == board[4][4] == board[2][2] == board[3][3] == 'x':
                if board[0][0] == "-":
                    board[0][0] = 'x'
                    x = False
                    break
                elif board[5][5] == "-":
                    board[5][5] = 'x'
                    x = False
                    break
            if board[0][1] == board[1][2] == board[2][3] == board[3][4] == 'x':
                if board[4][5] == "-":
                    board[4][5] = 'x'
                    x = False
                    break
            if board[4][5] == board[3][4] == board[2][3] == board[1][2] == 'x':
                if board[0][1] == "-":
                    board[0][1] = 'x'
                    x = False
                    break
            if board[1][0] == board[2][1] == board[3][2] == board[4][3] == 'x':
                if board[5][4] == "-":
                    board[5][4] = 'x'
                    x = False
                    break
            if board[5][4] == board[4][3] == board[3][2] == board[2][1] == 'x':
                if board[1][0] == "-":
                    board[1][0] = 'x'
                    x = False
                    break
            for i in range(6):
                if board[i][0] == board[i][1] == board[i][2] == board[i][3] == 'o':
                    if board[i][4] == "-":
                        board[i][4] = 'o'
                        x = False
                        break
                if board[i][5] == board[i][4] == board[i][2] == board[i][3] == 'o':
                    if board[i][1] == "-":
                        board[i][1] = 'o'
                        x = False
                        break
                if board[i][1] == board[i][2] == board[i][3] == board[i][4] == 'o':
                    if board[i][5] == "-":
                        board[i][5] = 'o'
                        x = False
                        break
                    elif board[i][0] == "-":
                        board[i][0] = 'o'
                        x = False
                        break
                if board[0][i] == board[1][i] == board[2][i] == board[3][i] == 'o':
                    if board[4][i] == "-":
                        board[4][i] = 'o'
                        x = False
                        break
                if board[5][i] == board[4][i] == board[2][i] == board[3][i] == 'o':
                    if board[1][i] == "-":
                        board[1][i] = 'o'
                        x = False
                        break
                if board[1][i] == board[2][i] == board[3][i] == board[4][i] == 'o':
                    if board[5][i] == "-":
                        board[5][i] = 'o'
                        x = False
                        break
                    elif board[0][i] == "-":
                        board[0][i] = 'o'
                        x = False
                        break

            if board[0][0] == board[1][1] == board[2][2] == board[3][3] == 'o':
                if board[4][4] == "-":
                    board[4][4] = 'o'
                    x = False
                    break
            if board[5][5] == board[4][4] == board[2][2] == board[3][3] == 'o':
                if board[1][1] == "-":
                    board[1][1] = 'o'
                    x = False
                    break
            if board[1][1] == board[2][2] == board[4][4] == board[3][3] == 'o':
                if board[0][0] == "-":
                    board[0][0] = 'o'
                    x = False
                    break
                elif board[5][5] == "-":
                    board[5][5] = 'o'
                    x = False
                    break
            if board[0][1] == board[1][2] == board[2][3] == board[3][4] == 'o':
                if board[4][5] == "-":
                    board[4][5] = 'o'
                    x = False
                    break
            if board[4][5] == board[3][4] == board[2][3] == board[1][2] == 'o':
                if board[0][1] == "-":
                    board[0][1] = 'o'
                    x = False
                    break
            if board[1][0] == board[2][1] == board[3][2] == board[4][3] == 'o':
                if board[5][4] == "-":
                    board[5][4] = 'o'
                    x = False
                    break
            if board[5][4] == board[4][3] == board[3][2] == board[2][1] == 'o':
                if board[1][0] == "-":
                    board[1][0] = 'o'
                    x = False
                    break

            row = random.choice(position_row)
            collum = random.choice(position_collum)
            
            if board[row][collum] == '-':
                board[row][collum] = 'x'
                x = False

    def check_order_win(self):
           '''
           Function that checks if there are 5 consecutive symbols in te same orientation
           If there is then it will return True
           :return:
           '''
           for i in range(6):

               if self.game_board[i][5] == self.game_board[i][1] == self.game_board[i][2] == self.game_board[i][3] == self.game_board[i][4] == 'x':
                   return True

               if self.game_board[5][i] == self.game_board[1][i] == self.game_board[2][i] == self.game_board[3][i] == self.game_board[4][i] == 'x':
                   return True
               if self.game_board[i][0] == self.game_board[i][1] == self.game_board[i][2] == self.game_board[i][3] == self.game_board[i][4] == 'x':
                   return True
               if self.game_board[0][i] == self.game_board[1][i] == self.game_board[2][i] == self.game_board[3][i] == self.game_board[4][i] == 'x':
                   return True

           for i in range(2):
               if self.game_board[i][i] == self.game_board[i+1][i+1] == self.game_board[i+2][i+2] == self.game_board[i+3][i+3] == self.game_board[i+4][i+4] == 'x':
                   return True



           if self.game_board[1][0] == self.game_board[2][1] == self.game_board[3][2] == self.game_board[4][3] == self.game_board[5][4] == 'x':
               return True
           if self.game_board[0][1] == self.game_board[1][2] == self.game_board[2][3] == self.game_board[3][4] == self.game_board[4][5] == 'x':
               return True

           for i in range(2):
               if self.game_board[i][5-i] == self.game_board[i+1][4-i] == self.game_board[i+2][3-i] == self.game_board[i+3][2-i] == self.game_board[i+4][1-i] == 'x':
                   return True
           if self.game_board[1][5] == self.game_board[2][4] == self.game_board[3][3] == self.game_board[4][2] == self.game_board[5][1] == 'x':
               return True

           if self.game_board[0][4] == self.game_board[1][3] == self.game_board[2][2] == self.game_board[3][1] == self.game_board[4][0] == 'x':
               return True


           for i in range(6):

               if self.game_board[5][i] == self.game_board[1][i] == self.game_board[2][i] == self.game_board[3][i] == self.game_board[4][i] == 'o':
                   return True
               if self.game_board[0][i] == self.game_board[1][i] == self.game_board[2][i] == self.game_board[3][i] == self.game_board[4][i] == 'o':
                   return True

               if self.game_board[i][5] == self.game_board[i][1] == self.game_board[i][2] == self.game_board[i][3] == \
                       self.game_board[i][4] == 'o':
                   return True
               if self.game_board[i][0] == self.game_board[i][1] == self.game_board[i][2] == self.game_board[i][3] == self.game_board[i][4] == 'o':
                   return True
           for i in range(2):
               if self.game_board[i][i] == self.game_board[i + 1][i + 1] == self.game_board[i + 2][i + 2] == self.game_board[i + 3][i + 3] == self.game_board[i + 4][i + 4] == 'o':
                   return True

           if self.game_board[0][1] == self.game_board[1][2] == self.game_board[2][3] == self.game_board[3][4] ==  self.game_board[4][5] == 'o':
               return True

           if self.game_board[1][0] == self.game_board[2][1] == self.game_board[3][2] == self.game_board[4][3] == self.game_board[5][4] == 'o':
               return True

           for i in range(2):
               if self.game_board[i][5 - i] == self.game_board[i + 1][4 - i] == self.game_board[i + 2][3 - i] == self.game_board[i + 3][2 - i] == self.game_board[i + 4][1 - i] == 'o':
                   return True

           if self.game_board[0][4] == self.game_board[1][3] == self.game_board[2][2] == self.game_board[3][1] == self.game_board[4][0] == 'o':
               return True

           if self.game_board[1][5] == self.game_board[2][4] == self.game_board[3][3] == self.game_board[4][2] == self.game_board[5][1] == 'o':
               return True

           return False




    def check_chaos_win(self):
        for i in range(6):
            for j in range(6):
                if self.game_board[i][j] == "-":
                    return False
        return True


       
