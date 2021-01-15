import pygame
from menu import GameMenu, SettingsMenu


pygame.init()
surface = pygame.display.set_mode((600, 500))
settings_menu = SettingsMenu()
game_menu = GameMenu(settings_menu)
game_menu.mainloop(surface)