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
game_menu.enable()

# init entities
# init snake
snake = pygame.sprite.LayeredUpdates()
snake_head = Snake("textures/snake_head.png", 300, 250, 0)
snake.add(snake_head)


# init food
food_sprite = pygame.sprite.Group()
food = Food()
food_sprite.add(food)
food_sprite.update()

# init borders
borders = pygame.sprite.Group()
border = Borders()
borders.add(border)

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
    # launching the menu
    if game_menu.is_enabled():
        game_menu.mainloop(surface)

    # init object for displaying score
    score_disp = font.render(f'Score: {score}', 1, (255, 215, 0))
    # FPS
    clock.tick(5)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        # game instruction
        if event.type == pygame.KEYDOWN:
            # snake movement
            # change the direction and remember
            if event.key == pygame.K_LEFT and last_mov != "RIGHT":
                x_mov = -15
                y_mov = 0
                last_mov = "LEFT"
            elif event.key == pygame.K_RIGHT and last_mov != "LEFT":
                x_mov = 15
                y_mov = 0
                last_mov = "RIGHT"
            elif event.key == pygame.K_UP and last_mov != "DOWN":
                x_mov = 0
                y_mov = -15
                last_mov = "UP"
            elif event.key == pygame.K_DOWN and last_mov != "UP":
                x_mov = 0
                y_mov = 15
                last_mov = "DOWN"
            # pause
            elif event.key == pygame.K_ESCAPE:
                game_menu.enable()



    # stop game if snake touched the yourself
    if len(pygame.sprite.spritecollide(snake_head, snake, False)) > 1 and len(snake) > 3:
        running = False

    # stop game if snake touched the borders
    if pygame.sprite.collide_mask(snake_head, border):
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
        snake.add(Snake("textures/snake.png", tail_x, tail_y, len(snake)))
        # creating new food
        food_sprite.update()
    # update playing field
    surface.fill((0, 0, 0))
    food_sprite.draw(surface)
    snake.draw(surface)
    borders.draw(surface)
    surface.blit(score_disp, (0, 0))
    

    
    pygame.display.update()

pygame.quit()