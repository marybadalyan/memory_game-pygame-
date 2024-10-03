import pygame
import random
import time

snake_speed = 17

# pygame window
window_size_x = 600
window_size_y = 600

window_color = pygame.Color(102, 204, 0)
fruit_color = pygame.Color(255, 0, 0)
score_color = pygame.Color(0, 0, 0)
snake_color = pygame.Color(255, 255, 0)
# pygame setup
pygame.init()

pygame.display.set_caption("Snake Game")
game_window = pygame.display.set_mode((window_size_x, window_size_y))

# FPS (frames per second) controller 
fps = pygame.time.Clock()

snake_position = [100, 40]
snake_body = [[100, 40], [80, 40], [60, 40], [40, 40]]

direction = 'RIGHT'  # Start and go right
change_to = direction

score = 0
pixel_size = 20

def fruit_pos_rand():
    return [random.randrange(1, (window_size_x // pixel_size)) * pixel_size,
            random.randrange(1, (window_size_y // pixel_size))* pixel_size]

def show_score():
    score_font = pygame.font.SysFont("Comic Sans MS", 30)
    score_surface = score_font.render('Score: ' + str(score), True, score_color)
    score_rect = score_surface.get_rect()
    score_rect.midtop = (window_size_x // 2, 0)
    game_window.blit(score_surface, score_rect)

def game_over():
    game_over_font = pygame.font.SysFont("Comic Sans MS", 50)
    game_over_surface = game_over_font.render("GAME OVER", True, score_color)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_size_x / 2, window_size_y / 4)

    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

fruit_position = fruit_pos_rand()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            if event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            if event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'
            if event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
    
    # Update the direction
    direction = change_to

    # Move the snake
    if direction == 'RIGHT':
        snake_position[0] += pixel_size
    if direction == 'LEFT':
        snake_position[0] -= pixel_size
    if direction == 'UP':
        snake_position[1] -= pixel_size
    if direction == 'DOWN':
        snake_position[1] += pixel_size

    # Insert new head position
    snake_body.insert(0, list(snake_position))
    
    # Check if the snake has eaten the fruit
    if (snake_position[0]//pixel_size == fruit_position[0]//pixel_size) and (snake_position[1]//pixel_size == fruit_position[1]//pixel_size) :
        score += 10
        fruit_position = fruit_pos_rand()  # Spawn new fruit
    else:
        snake_body.pop()  # Remove last segment if not eating fruit

    game_window.fill(window_color)

    # Draw the snake
    for pos in snake_body:
        pygame.draw.rect(game_window, snake_color, pygame.Rect(pos[0], pos[1], pixel_size, pixel_size))

    # Draw the fruit
    pygame.draw.rect(game_window, fruit_color, pygame.Rect(fruit_position[0], fruit_position[1], pixel_size, pixel_size))

    # Check for wall collisions
    if (snake_position[0] < 0 or snake_position[0] > window_size_x - pixel_size or
        snake_position[1] < 0 or snake_position[1] >  window_size_y - pixel_size):
        game_over()

    # Check for collisions with itself
    for block in snake_body[1:]:
        if snake_position == block:
            game_over()

    show_score()
    pygame.display.update()
    fps.tick(snake_speed)
