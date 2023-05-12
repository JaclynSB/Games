import pygame, sys
import numpy as np
pygame.init()

#constant variables
size = 600
line = 5
row = 3
col = 3
sqr = size/3
circle_rad = sqr/3
circle_wid = 15
cross_wid = 25
space = 55
white = (255,255,255)
line_color = (0,0,0)
red = (255,0,0)
pink = (200, 100, 100)
teal = (23,145,135)
winner = ''

font = pygame.font.Font(None, int(size/16))
reminder = pygame.font.Font(None, int(size/32))


#screen and display
screen = pygame.display.set_mode([size,size+100])

pygame.display.set_caption('Tic-Tac-Toe by Jaclyn S-B')
screen.fill(white)

#create board
board = np.zeros((row,col))

#functions
def draw_lines():
    #horizontal lines
    pygame.draw.line(screen, line_color, (0, sqr), (size, sqr), line)
    pygame.draw.line(screen, line_color, (0, 2*sqr), (size, 2*sqr), line)
    #vertical lines
    pygame.draw.line(screen, line_color, (sqr, 0), (sqr, size), line)
    pygame.draw.line(screen, line_color, (2*sqr,0), (2*sqr, size), line)
    
def draw_figures():
    for i in range(row):
        for j in range(col):
            if board[i][j] == 1:
                pygame.draw.circle(screen, pink, (int(j*sqr + sqr/2), int(i*sqr + sqr/2)), circle_rad, circle_wid)
            elif board[i][j] == 2:
                pygame.draw.line(screen, teal, (j*sqr+space, i*sqr+sqr-space), (j*sqr+sqr-space, i*sqr+space), cross_wid)
                pygame.draw.line(screen, teal, (j*sqr+space, i*sqr+space), (j*sqr+sqr-space, i*sqr+sqr-space), cross_wid)

def whose_move(player):
    if player == 1:
        pygame.draw.rect(screen, white, pygame.Rect(0,size+1, size, 99))
        screen.blit(font.render('Next up: '+ 'O', True, line_color), (10, size+50))  
    elif player == 2:
        pygame.draw.rect(screen, white, pygame.Rect(0,size+1, size, 99))
        screen.blit(font.render('Next up: '+ 'X', True, line_color), (10, size+50)) 
    screen.blit(reminder.render('press r to restart', True, line_color), (size-(size/5), size+50))


def make_move(row,col,player):
    board[row][col] = player

def avail_square(row,col):
    return board[row][col] == 0

def board_full():
    for i in range(row):
        for j in range(col):
            if board[row][col] == 0:
                return False
            else:
                return True

def draw_vert_win(column, player):
    posX = column*sqr + sqr//2
    pygame.draw.line(screen, red, (posX, 15), (posX, size - 15), 10)
    
def draw_hor_win(row, player):
    posY = row*sqr + sqr//2   
    pygame.draw.line( screen, red, (15, posY), (size - 15, posY), 10)
    
def draw_asc_diagonal(plr):
    pygame.draw.line(screen, red, (15, size - 15), (size - 15, 15), 10)

def draw_desc_diagonal(plr):
    pygame.draw.line(screen, red, (15, 15), (size - 15, size - 15), 10)

def win(player):
    #vertical win
    for i in range(col):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            draw_vert_win(i, player)
            return True
    #horizontal win
    for j in range(row):
        if board[j][0] == player and board[j][1] == player and board[j][2] == player:
            draw_hor_win(j, player)
            return True
    #diagonal win
        if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            draw_desc_diagonal(player)
            return True
        if board[2][0] == player and board[1][1] == player and board[0][2] == player:
            draw_asc_diagonal(player)
            return True
    
def restart():
    screen.fill(white)
    draw_lines()
    for i in range(row):
        for j in range(col):
            board[i][j] = 0

draw_lines()
player = 1
whose_move(player)
running = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and running:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
        
            clicked_row = int(mouseY//sqr)
            clicked_col = int(mouseX//sqr)
            
            if avail_square(clicked_row, clicked_col):
                make_move(clicked_row, clicked_col, player)
                if win(player):
                    win_loc = pygame.draw.rect(screen, white, pygame.Rect(size/5, size+50, size/3, size/3))
                    text = 'Congratulations, you won '
                    if player == 1:
                        winner = 'O'
                    elif player == 2:
                        winner = 'X'
                    pygame.draw.rect(screen, white, pygame.Rect(0,size+1, size, 99))
                    screen.blit(font.render(text + str(winner) + '!', True, red), (win_loc.x, win_loc.y))
                    game_over = True
                else:   
                    player = player % 2 + 1
                    whose_move(player)
            
            draw_figures()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                player = 1
                whose_move(player)
                game_over = False

            
        pygame.display.update()


pygame.quit()
