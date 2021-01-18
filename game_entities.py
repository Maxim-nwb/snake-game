import pygame
import random

class Snake(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (300, 250)
        
    def update(self, x, y):
        self.rect.x += x
        self.rect.y += y

class Food(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x = random.randint(1, 599)
        self.rect.y = random.randint(1, 499)

