import pygame
import time
import random
import sys

pygame.init()

window_X = 300
window_Y = 300
yellow  = pygame.Color(255,255,0)
X_Color = pygame.Color(102,204,0)
O_Color = pygame.Color(255,51,51)
line_color = (0,0,0)
wondow_Color  = pygame.Color(0,204,102)
pixel_size = 100
line_thicknes = 7
space = 10
screen = pygame.display.set_mode((window_X,window_Y))  #sahmanuma chapery 
pygame.display.set_caption("Ttc-Tac-Toe")
screen.fill(yellow)
board = [[0,0,0],
         [0,0,0],
         [0,0,0]]


def draw_lines():
    
    pygame.draw.line(screen,line_color,(space,pixel_size),(window_X-space,pixel_size),line_thicknes)

    pygame.draw.line(screen,line_color,(space,pixel_size*2),(window_X-space,pixel_size*2),line_thicknes)

    pygame.draw.line(screen,line_color,(pixel_size,space),(pixel_size,window_Y-space),line_thicknes)

    pygame.draw.line(screen,line_color,(pixel_size*2,space),(pixel_size*2,window_Y-space),line_thicknes)


def avaliable(i,j):
    return board[i][j] == 0

def mark(i,j,s):
    board[i][j] = s


def draw_figures():
    for i in range(3):
        for j in range(3):
            if board[i][j] == 1:
                pygame.draw.circle(screen,O_Color,(j*pixel_size + pixel_size//2, i*pixel_size + pixel_size//2),47,5)
            elif board[i][j] == 2: 
                pygame.draw.line(screen,X_Color,(j*pixel_size + space,i*pixel_size + space),(j*pixel_size + pixel_size - space, i*pixel_size + pixel_size  - space),line_thicknes)
                pygame.draw.line(screen,X_Color,(j*pixel_size+space,i*pixel_size+pixel_size-space),(j*pixel_size+pixel_size-space,i*pixel_size+space),line_thicknes)

def draw_vertical(col,p):
    posS = col*pixel_size + pixel_size//2

    if p == 1:
        color = X_Color
    else:
        color = O_Color 
           
    pygame.draw.line(screen,color,(posS,space),(posS,window_X - space),line_thicknes)

def board_full():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                return False
    return True

def draw_horizontal(row,p):
    posS = row*pixel_size + pixel_size//2

    if p == 1:
        color = X_Color
    else:
        color = O_Color 

    pygame.draw.line(screen,color,(space,posS),(window_Y-space,posS),line_thicknes)

    
def draw_asc_diagonal(p):
    if p == 1:
        color = X_Color
    else:
        color = O_Color 

    pygame.draw.line(screen,color,(space,space),(window_Y-space,window_Y-space),line_thicknes)
    
def  draw_dec_diagonal(p):
    if p == 1:
        color = X_Color
    else:
        color = O_Color 
    
    pygame.draw.line(screen,color,(space,window_X-space),(window_Y-space,space),line_thicknes)


def check_win(p):
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == p:
            draw_figures()
            draw_vertical(col,p)
            return True
        
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == p:
            draw_figures()
            draw_horizontal(row,p)
            return True
    
    if board[0][0] == board[1][1] == board[2][2] == p:
        draw_figures()
        draw_asc_diagonal(p)
        return True
    
    if board[0][2] == board[1][1] == board[2][0] == p:
        draw_figures()
        draw_dec_diagonal(p)
        return True
   

def game_over(i):
    pygame.display.flip()
    time.sleep(0.3)

    screen.fill(line_color)
    
    game_over_text = pygame.font.SysFont('Comic Sans MS',30)
    if i == 0:
        game_over_surface = game_over_text.render("NO_WIN",True,yellow)
    elif i == 1:
        game_over_surface = game_over_text.render("Player 1 Wins!",True,yellow)
    else:
        game_over_surface = game_over_text.render("Player 2 Wins!",True,yellow)

    game_over_rect = game_over_surface.get_rect()
    game_over_rect.center = (window_X//2,window_Y//2)

    screen.blit(game_over_surface,game_over_rect)

    pygame.display.flip() 
    time.sleep(1)
    pygame.quit()

    quit()


draw_lines()
playing = True
player = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and playing:
            clk_column = (event.pos[0])//pixel_size
            clk_row = (event.pos[1])//pixel_size
            
            if avaliable(clk_row,clk_column):
                mark(clk_row,clk_column,player)

                if check_win(player):
                    playing = False
                    game_over(player)
                player = player%2 + 1
                draw_figures()

        if board_full():
            game_over(0)

    
    pygame.display.update()



                
            

                   

                
