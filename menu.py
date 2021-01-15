import pygame_menu
import pygame


class GameMenu(pygame_menu.Menu):
    def __init__(self, settings):
        super().__init__(400, 500, 'MENU', theme=pygame_menu.themes.THEME_BLUE)
        self.create_widgets(settings)

    def create_widgets(self, settings):
        self.add_button('Play', pygame_menu.events.CLOSE)
        self.add_button('Settings', settings)
        self.add_button('Quit', pygame_menu.events.EXIT)


class SettingsMenu(pygame_menu.Menu):
    def __init__(self):
        super().__init__(400, 500, 'SETTINGS', theme=pygame_menu.themes.THEME_BLUE)
        self.create_widgets()

    def create_widgets(self):
        self.add_text_input('Player: ', default='Username')
        self.add_selector(title="Snake Color: ", 
                          items=[
                                 ('Black', (0, 0, 0)),
                                 ('Blue', (12, 12, 200))
                                 ], 
                          )
        self.add_selector("Background Color: ", 
                          items=[
                                 ('Black', (0, 0, 0)),
                                 ('Blue', (12, 12, 200))
                                 ]
                          )
        self.add_button('Back', pygame_menu.events.BACK)