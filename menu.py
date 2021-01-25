import pygame_menu
import pygame
import pickle


class GameMenu(pygame_menu.Menu):
    # main menu
    # displayed at the beginning or on restart 
    def __init__(self, settings):
        super().__init__(400, 500, 'MENU', theme=MyTheme)
        self.create_widgets(settings)

    def create_widgets(self, settings):
        self.add_button('Play', self.disable)
        self.add_button('Settings', settings)
        self.add_button('Quit', pygame_menu.events.EXIT)



class SettingsMenu(pygame_menu.Menu):
    # settings menu of the game
    def __init__(self, SETTINGS):
        super().__init__(400, 500, 'SETTINGS', theme=MyTheme)
        self.USERNAME = SETTINGS["USERNAME"]
        self.BACKGROUND_COLOR = SETTINGS["BACKGROUND_COLOR"]
        self.DIFFICULTY = SETTINGS["DIFFICULTY"]
        self.create_widgets()

    def create_widgets(self):

        self.add_label("Attention!\nSettings will be applied after restarting the game!",
                       **{'font_size': 30, 'font_color': (255, 0, 0)})

        self.add_text_input('Player: ', default=self.USERNAME, onchange=self.change_user)

        self.add_selector("Background Color: ", 
                          items=[
                                 ('Black', (0, 0, 0)),
                                 ('White', (255, 255, 255)),
                                 ('Red', (255, 0, 0)),
                                 ('Blue', (0, 0, 255))
                                 ],
                          default=self.BACKGROUND_COLOR[-1],
                          onchange=self.change_color
                          )

        self.add_selector('Difficulty', items=[
                                 ('Easy', 0),
                                 ('Middle', 1),
                                 ('Hard', 2),
                                 ],
                          default=self.DIFFICULTY[-1],
                          onchange=self.change_difficulty)

        self.add_button('Save', self.save_data)
        self.add_label("", "saving_label", 
                       **{'font_size': 30, 'font_color': (255, 0, 0)})

    # save settings
    def change_difficulty(self, *value):
        self.DIFFICULTY = value[0][0]

    def change_user(self, *value):
        self.USERNAME = value[0]

    def change_color(self, *value):
        self.BACKGROUND_COLOR = (value[-1], value[0][1])

    def save_data(self):
        with open('settings.dat', 'wb') as f:
            settings = { "USERNAME" : self.USERNAME,
                         "BACKGROUND_COLOR" : self.BACKGROUND_COLOR,
                         "DIFFICULTY" : self.DIFFICULTY
                        }
            pickle.dump(settings, f)
        self.get_widget("saving_label").set_title("Settings saved!")


class PauseMenu(pygame_menu.Menu):
    # Pause menu
    # shown when you press "Esc" during the game
    def __init__(self):
        super().__init__(300, 500, 'Pause', theme=MyTheme, enabled=False)
        self.create_widgets()

    def create_widgets(self):
        self.add_label("", "user_info", 
                       **{'font_size': 30, 'font_color': (255, 105, 180), 'margin': (0, 20)})

        self.add_button('Continue', self.disable)
        
        self.add_button('Quit the game', pygame_menu.events.EXIT)


class DeadMenu(pygame_menu.Menu):
    # Game over menu
    # Displayed at death
    def __init__(self):
        super().__init__(340, 400, '', theme=MyTheme, enabled=False)
        self.create_widgets()

    def create_widgets(self):
        self.add_label("GAME OVER!", **{'font_size': 100, 'font_color': (255, 0, 0)})
        self.add_label("", "score", 
                       **{'font_size': 30, 'font_color': (255, 105, 180), 'margin': (0, 20)})
        self.add_button('Back to main menu', self.disable)
        self.add_button('Quit the game', pygame_menu.events.EXIT)

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