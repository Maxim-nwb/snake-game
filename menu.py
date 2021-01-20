import pygame_menu
import pygame


class GameMenu(pygame_menu.Menu):
    def __init__(self, settings):
        super().__init__(400, 500, 'MENU', theme=MyTheme)
        self.create_widgets(settings)

    def create_widgets(self, settings):
        self.add_button('Play', self.disable)
        self.add_button('Settings', settings)
        self.add_button('Quit', pygame_menu.events.EXIT)



class SettingsMenu(pygame_menu.Menu):
    def __init__(self):
        super().__init__(400, 500, 'SETTINGS', theme=MyTheme)
        self.create_widgets()

    def create_widgets(self):
        self.add_text_input('Player: ', default='Username')
        self.add_selector(title="Snake Color: ", 
                          items=[
                                 ('Black', (0, 0, 0)),
                                 ('White', (255, 255, 255)),
                                 ('Green', (0, 255, 0)),
                                 ('Red', (255, 0, 0)),
                                 ('Blue', (12, 12, 200))
                                 ], 
                          )
        self.add_selector("Background Color: ", 
                          items=[
                                 ('Black', (0, 0, 0)),
                                 ('White', (255, 255, 255)),
                                 ('Green', (0, 255, 0)),
                                 ('Red', (255, 0, 0)),
                                 ('Blue', (12, 12, 200))
                                 ]
                          )
        self.add_button('Save', pygame_menu.events.CLOSE)



#Theme
MyTheme = pygame_menu.themes.Theme(
        background_color=(154, 205, 50),
        title_font_color=(255, 105, 180),
        title_background_color=(255, 215, 0),
        title_font=pygame_menu.font.FONT_FRANCHISE,
        title_font_size=60,
        widget_font=pygame_menu.font.FONT_FRANCHISE,
        widget_font_color=(170, 170, 170),
        widget_font_size=45,
        widget_shadow=False,
        widget_shadow_position=pygame_menu.locals.POSITION_SOUTHEAST
)