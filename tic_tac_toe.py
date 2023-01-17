import random

class TicTacToe:
    def __init__(self):
        self.board = []
        self.free = ' '
        self.x = 'X'
        self.o = 'O'
        self.cnt = 0
        self.next = ''


    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append(self.free)
            self.board.append(row)
        # return self.board
    
    def isfree(self, row, col):
        if self.board[row-1][col-1] == (self.free):
            return True
        else:
            return False

    def nextplayer(self):
        num = random.randint(0,1)
        if self.cnt == 0:
            if num == 0:
                self.next = self.x
            elif num == 1:
                self.next = self.o
        else:
            if self.cnt % 2 == 0:
                if self.next == self.x:
                    self.next = self.o
                else:
                    self.next = self.x
            else:
                if self.next == self.x:
                    self.next = self.o
                else:
                    self.next = self.x
        self.cnt += 1
        return self.next  

    def loc(self, player, row, col):
        if self.isfree(row, col) == True:
            self.board[row-1][col-1] = self.next
        else:
            print('Sorry, that spot is taken. Try again.')
            self.cnt -= 1

    def show_board(self):
        for i in self.board:
            print(i)
        return ' '

    def win(self):
        win = None
        n = len(self.board)
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != self.next:
                    win = False
                    break
            if win:
                return win
        # columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != self.next:
                    win = False
                    break
            if win:
                return win
        # diagonals
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][i] != self.next:
                    win = False
                    break
        if win:
            return win
        for i in range(n):
            win == True
            for j in range(n):
                if self.board[i][2-i] != self.next:
                    win = False
                    # break
        if win:
            return win

    
    def play(self):
        self.nextplayer()
        print("Let's play Tic Tac Toe!", self.next, "will go first. Here is the board:")
        self.create_board()
        print(self.show_board())

        for i in range(9):
            print("Player", self.next, "please pick your target row 1-3:")
            row = int(input())
            print("Okay, now pick your target column 1-3:")
            col = int(input())
            if self.isfree(row, col) == True:
                self.loc(self.next, row, col)
                if self.win() == True:
                    print("Congratulations,", self.next, "you won!")
                    print(self.show_board())
                    break
                else:
                    print(self.show_board())
                    self.nextplayer()
            else:
                self.loc(self.next, row, col)
                print(self.show_board())
            

ttt = TicTacToe()
ttt.play()
