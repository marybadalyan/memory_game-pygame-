import pygame 
import time
import random

pygame.init()
"""
Create a game that matches colors together as cards. 
We need to have a board where, every time you click on any 
of the cards, they turn a certain color. If two card 
colors match, they get removed from the board.

Required functionalities:
- Take the inputs and check if certain colors match.
- Create a function that draws colors on each card. 
  Colors can have numbers associated with them, and 
  the board indices can store those numbers.
- Every time an input is taken, the individual card 
  should be revealed, so we need a function called `open_card`.
- Create a separate `draw_board` function.
- Implement an `is_match` function that will check if two selected
  cards on the board (identified by their row and column) match. If 
  they do, erase the corresponding cards.
"""

width = 400
heigth = 430
pixel_size = 100
#colors 8colores
color_0 = pygame.Color(0,255,255)
color_1 = pygame.Color(255,255,0)
color_2 = pygame.Color(255,128,0)
color_3 = pygame.Color(255,0,0)
color_4 = pygame.Color(0,255,0)
color_5 = pygame.Color(0,0,255)
color_6 = pygame.Color(102,0,204)
color_7 = pygame.Color(204,0,102)
colors = [color_0,color_1,color_2,color_3,color_4,color_5,color_6,color_7]
screen_color = pygame.Color(65,65,65)
color_empty = pygame.Color(0,0,0)
line_color = pygame.Color(128,128,128)
text_color = pygame.Color(255,255,255)
line_thicknes = 3
#draw the board 4*4
board = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]
avalable_cordinates = [[0,0],[0,1],[0,2],[0,3],
                       [1,0],[1,1],[1,2],[1,3],
                       [2,0],[2,1],[2,2],[2,3],
                       [3,0],[3,1],[3,2],[3,3]]


screen = pygame.display.set_mode((width,heigth))
pygame.display.set_caption("Memory Game")
score = 0

def draw_lines():
    for i in range(3):
        pygame.draw.line(screen,line_color,(i*pixel_size+pixel_size,0),(i*pixel_size+pixel_size,width),line_thicknes)
    for i in range(4):
        pygame.draw.line(screen,line_color,(0,i*pixel_size+pixel_size),(heigth,i*pixel_size+pixel_size),line_thicknes)

def draw_card(x,y,color):
        pygame.draw.rect(screen,color,pygame.Rect(y*pixel_size,x*pixel_size,pixel_size,pixel_size))
        draw_lines()
        pygame.display.flip()
            
       
def show_score(score):
    # Clear the previous score area before drawing the new score
    pygame.draw.rect(screen, screen_color, pygame.Rect(150, 410, 100, 30))
    score_font = pygame.font.SysFont("Comic Sans MS", 20)
    score_surface = score_font.render(f"Score: {score}", True,text_color)
    score_rect = score_surface.get_rect(midbottom=(200, 430))
    screen.blit(score_surface, score_rect)
    pygame.display.update()
    
def win():
    pygame.draw.rect(screen,screen_color,pygame.Rect(150,410,100,30))
    win_font = pygame.font.SysFont("Comic Sans MS", 20)
    win_text = win_font.render("You have won",True,text_color)
    win_rect = win_text.get_rect(midbottom=(200,430))
    screen.blit(win_text,win_rect)
    pygame.display.update() 

def randomize_board():
    for i in range(8):
        for j in range(2):
            cord = avalable_cordinates[random.randrange(0,len(avalable_cordinates))]
            board[cord[0]][cord[1]] = i
            avalable_cordinates.remove(cord)


def is_match(x1,y1,x2,y2):
    if board[x1][y1] == board[x2][y2]:
        return True

screen.fill(screen_color)

randomize_board()
first_click = None
playing =True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.pos[1] <= 400:    
            y,x = event.pos[0]//pixel_size, event.pos[1]//pixel_size
            
            if board[x][y] == 'x':
                break

            if first_click == None:
                first_click = (x,y)
                draw_card(first_click[0],first_click[1],colors[board[x][y]])
                click_time = time.time()
            elif first_click != (x,y):
                draw_card(x,y,colors[board[x][y]])
                time.sleep(0.5)

                if is_match(first_click[0],first_click[1],x,y):
                    draw_card(x,y,color_empty)
                    draw_card(first_click[0],first_click[1],color_empty)
                    board[first_click[0]][first_click[1]] = 'x' 
                    board[x][y] = 'x'
                    score += 1
                else: 
                    draw_card(first_click[0],first_click[1],screen_color)
                    draw_card(x,y,screen_color)
                first_click = None  

        if  first_click != None and time.time() - click_time >= 0.8:
            draw_card(first_click[0],first_click[1],screen_color)
            first_click = None
    
    draw_lines()
    show_score(score)
    if score==8:
        time.sleep(1)
        win()
        playing = False
    pygame.display.update()
  
pygame.quit()
quit()





