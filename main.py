import pygame
from menu import GameMenu, SettingsMenu
from game_entities import *


# init game
pygame.init()
surface = pygame.display.set_mode((600, 500))
clock = pygame.time.Clock()

# init menu
settings_menu = SettingsMenu()
game_menu = GameMenu(settings_menu)

# init entities
# init snake
snake = pygame.sprite.LayeredUpdates()
snake_head = Snake(300, 250, 0)
snake.add(snake_head)
food_sprite = pygame.sprite.Group()

# init food
food = Food()
food_sprite.add(food)
food_sprite.update()

# init score
score = 0
font = pygame.font.SysFont(None, 36)

# variable for controlling movements
x_mov = 0       
y_mov = 0
last_mov = None # last direction of movement
# variable for loop control
running = True

# game loop
while running:
    # init object for displaying score
    score_disp = font.render(f'Score: {score}', 1, (165, 42, 42))
    # FPS
    clock.tick(5)
    #game_menu.mainloop(surface)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        # snake movements
        # change the direction and remember
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and last_mov != "RIGHT":
                x_mov = -10
                y_mov = 0
                last_mov = "LEFT"
            elif event.key == pygame.K_RIGHT and last_mov != "LEFT":
                x_mov = 10
                y_mov = 0
                last_mov = "RIGHT"
            elif event.key == pygame.K_UP and last_mov != "DOWN":
                x_mov = 0
                y_mov = -10
                last_mov = "UP"
            elif event.key == pygame.K_DOWN and last_mov != "UP":
                x_mov = 0
                y_mov = 10
                last_mov = "DOWN"

    # stop game if snake touched the yourself
    if len(snake.get_sprites_at((snake_head.rect.x, snake_head.rect.y))) > 1 and len(snake) > 2:
        running = False

    # stop game if snake touched the borders
    if snake_head.rect.x >= 600 or snake_head.rect.x < 0 or snake_head.rect.y >= 500 or snake_head.rect.y < 0:
        running = False

    # update screen
    snake.update(x_mov, y_mov)
    if food.chek_eating(snake_head):
        # adding points
        score += 1
        # get coordinates of the last element of the snake
        tail_x = snake.get_sprite(-1).rect.x
        tail_y = snake.get_sprite(-1).rect.y
        # adding a new element of the snake
        snake.add(Snake(tail_x, tail_y, len(snake)))
        # creating new food
        food_sprite.update()
    # update playing field
    surface.fill((0, 0, 0))
    surface.blit(score_disp, (0, 0))
    food_sprite.draw(surface)
    snake.draw(surface)
    
    pygame.display.flip()

pygame.quit()