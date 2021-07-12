#Import pygame,sys and numpy modules
import pygame, sys
import numpy as np
from pygame import gfxdraw
#Initialize pygame
pygame.init()

WIDTH = 600 #width of screen
HEIGHT = 600 #height of screen
LINE_WIDTH = 15 #width of lines
BG_COLOR = (6, 11, 26) #black
LINE_COLOR = (26, 26, 44) #dark navy
X_COLOR = (255, 255, 255) #white
O_COLOR = (94, 92, 190) #slate blue
BOARD_ROWS = 3 #Number of rows on the board
BOARD_COLS = 3 #Number of columns on the board
CIRCLE_RADIUS = 60 #Radius of circle
SMALL_RADIUS = 40 #Radius of inner small circle
X_WIDTH = 55 #Width of each of the lines that form the X shape
CROSS_WIDTH = 25 #X width
SPACE = 48 #Spacing

screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('Tic-Tac-Toe (Dark Mode) - By Pathum Danthanarayana')
screen.fill(BG_COLOR)

#Board
board = np.zeros( (BOARD_ROWS, BOARD_COLS) )


#Function to draw 4 main lines
def draw_lines():
    # 1 horizontal
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
    # 2 horizontal
    pygame.draw.line(screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)
    # 1 vertical
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
    # 2 vertical
    pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)


#Draw x's and o's
def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.gfxdraw.aacircle(screen, int(col * 200 + 100), int(row * 200 + 100), CIRCLE_RADIUS, X_COLOR)
                pygame.gfxdraw.filled_circle(screen, int(col * 200 + 100), int(row * 200 + 100), CIRCLE_RADIUS, X_COLOR)
                pygame.gfxdraw.aacircle(screen, int(col * 200 + 100), int(row * 200 + 100), SMALL_RADIUS, BG_COLOR)
                pygame.gfxdraw.filled_circle(screen, int(col * 200 + 100), int(row * 200 + 100), SMALL_RADIUS, BG_COLOR)
            elif board[row][col] == 2:
                pygame.draw.line(screen,  O_COLOR, (col * 200 + SPACE, row *200 +200 - SPACE), (col * 200 + 200 - SPACE, row * 200 + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, O_COLOR, (col * 200 + SPACE, row * 200 + SPACE), (col * 200 + 200 - SPACE, row * 200 + 200 - SPACE), CROSS_WIDTH)


#Function to mark squares which players choose to place x or o
def mark_square(row, col, player):
    board[row][col] = player

#Function to check if the desired square is available
def available_square(row, col):
    if board[row][col] == 0:
        return True
    else:
        return False

#Function to check if the board is full (* A 0 represents a free square, and a 1 represents a full/occupied square)
def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True

#Function to check if player has won
def check_win(player):
    #vertical win check
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col, player)
            return True
    #horizontal win check
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row, player)
            return True
    #asc diagonal win check
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        return True
    #desc diagonal win check
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        return True

    return False

#Function to draw vertical line through shapes to indicate a player has won
def draw_vertical_winning_line(col, player):
    posX = col * 200 + 100

    if player == 1:
        color = X_COLOR
    elif player == 2:
        color = O_COLOR
    
    pygame.draw.line(screen, color, (posX, 15), (posX, HEIGHT - 15), 15)

#Function to draw horizontal line through shapes to indicate a player has won
def draw_horizontal_winning_line(row, player):
    posY = row * 200 + 100

    if player == 1:
        color = X_COLOR
    
    elif player == 2:
        color = O_COLOR

    pygame.draw.line(screen, color, (15, posY), (WIDTH - 15, posY), 15)

#Function to draw ascending diagonal line through shapes to indicate a win
def draw_asc_diagonal(player):
    if player == 1:
        color = X_COLOR
    
    elif player == 2:
        color = O_COLOR
    
    pygame.draw.line(screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), 15)

#Function to draw descending diagonal line through shapes to indicate a win
def draw_desc_diagonal(player):
    if player == 1:
        color = X_COLOR
    
    elif player == 2:
        color = O_COLOR

    pygame.draw.line(screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), 15)

def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    player = 1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0


#Mainscript
draw_lines()


#Player variables
player = 1
game_over = False

#Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #Link console board to screen board
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0] #x-coordinate
            mouseY = event.pos[1] #y-coordinate

            clicked_row = int(mouseY // 200)
            clicked_col = int(mouseX // 200)

            if available_square(clicked_row, clicked_col):
                if player == 1:
                    mark_square(clicked_row, clicked_col, 1)
                    if check_win(player):
                        game_over = True
                    player = 2
                elif player == 2:
                    mark_square(clicked_row, clicked_col, 2)
                    if check_win(player):
                        game_over = True
                    player = 1
                
                draw_figures()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                player = 1
                game_over = False
    pygame.display.update()