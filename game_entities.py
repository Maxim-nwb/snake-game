import pygame
import random

class Snake(pygame.sprite.Sprite):
    def __init__(self, texture, x, y, index):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(texture), (15, 15))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # coordinates of the previous step
        self.x_last = None
        self.y_last = None
        # index in the sprite group
        self.index = index
        
    def update(self, x, y):
        # if the head, then sets the movement
        if self.index == 0:
            self.x_last = self.rect.x
            self.y_last = self.rect.y
            self.rect.x += x
            self.rect.y += y
        # otherwise, follows the top body
        else:
            top_body = self.groups()[0].get_sprite(self.index - 1)
            self.x_last = self.rect.x
            self.y_last = self.rect.y
            self.rect.x = top_body.x_last
            self.rect.y = top_body.y_last

class Food(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((15, 15))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()

    def chek_eating(self, other):
        # checking that the player has eaten the food
        x = other.rect.x
        y = other.rect.y
        if (self.rect.x in range(x - 10, x + 10, 1)) and (self.rect.y in range(y - 10, y + 10, 1)):
            return True
        else:
            return False

    def update(self):
        self.rect.x = random.randint(1, 590)
        self.rect.y = random.randint(1, 490)

