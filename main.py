import pygame
from menu import GameMenu, SettingsMenu
from game_entities import *



pygame.init()
surface = pygame.display.set_mode((600, 500))
clock = pygame.time.Clock()
# init menu
settings_menu = SettingsMenu()
game_menu = GameMenu(settings_menu)
# init entities
all_sprites = pygame.sprite.Group()
snake = Snake()
all_sprites.add(snake)

# variable for controlling movements
x_mov = 0       
y_mov = 0
# variable for loop control
running = True
while running:
    clock.tick(10)
    # game_menu.mainloop(surface)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        # snake movements
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_mov = -10
                y_mov = 0
            elif event.key == pygame.K_RIGHT:
                x_mov = 10
                y_mov = 0
            elif event.key == pygame.K_UP:
                x_mov = 0
                y_mov = -10
            elif event.key == pygame.K_DOWN:
                x_mov = 0
                y_mov = 10

    # stop game if snake touched the borders
    if snake.rect.x >= 600 or snake.rect.x < 0 or snake.rect.y >= 500 or snake.rect.y < 0:
        running = False

    # update screen
    all_sprites.update(x_mov, y_mov)
    surface.fill((0, 0, 0))
    all_sprites.draw(surface)
    
    pygame.display.flip()

pygame.quit()