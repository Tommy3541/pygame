import pygame
from utility import image_cutter

class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super().__init__()
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.image = pygame.image.load("assets/gameobjects/hrnec.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom=(self.x, self.y))

class Coins(GameObject):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
        self.image = pygame.image.load("assets/gameobjects/hrnec.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom=(self.x, self.y))     

class Sud(GameObject):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
        self.image = pygame.image.load("assets/gameobjects/sud.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom=(self.x, self.y))     
