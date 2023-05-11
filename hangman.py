
class Hangman:
    def __init__(self):
        self.man = ' '
        self.miss = 0
        self.cnt = 0
        self.word = ''
        self.p1 = ''
        self.p2 = ''
        self.guess = []
        
    def board(self):
        for i in range(len(self.word)):
            self.guess.append('_')
        
    def introScript(self):
        print('Hello, Player 1! What is your name?')
        Player1 = input()
        self.p1 = Player1
        print('Hello, ', Player1 + '. Welcome to Hangman! What word would you like Player 2 to work with?')
        word = input()
        self.word = word
        print('Got it.')
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        print('Hello, Player 2! What is your name?')
        Player2 = input()
        self.p2 = Player2
        print('Hello,', Player2 + ', welcome to Hangman! Let us begin.')
        print('There are', len(self.word), 'letters in your word')
        self.board()
        print(self.guess)
        self.cnt += 1


    def mistake(self):
        if self.miss == 1:
            self.man = 'O'
        if self.miss == 2:
            self.man = '0\n|'
        if self.miss == 3:
            self.man = ' O\n\|'
        if self.miss == 4:
            self.man = ' O\n\|/'
        if self.miss == 5:
            self.man = ' O\n\|/\n /'
        if self.miss == 6:
            self.man = ' O\n\|/\n /\ '



    def guess_word(self):
        print(self.p2 +',', 'please select a letter.')
        letter = input()
        if letter in self.word:
            print('Nice work!')
            for i in range(len(self.word)):
                if self.word[i] == letter:
                    self.guess[i] = letter
        else:
            print('Not quite.')
            self.miss += 1
            self.mistake()
            
        print(self.man, '\n')
        print(self.guess)  
        print('\n\n')  
        
        
    def play(self):
        for i in range(15):
            if self.cnt == 0:
                self.introScript()
            else:
                self.guess_word()
                if self.miss > 6:
                    print('\n SORRY, YOU LOSE! LOVE YOU ANYWAY')
                    break

        
hm = Hangman()
hm.play()