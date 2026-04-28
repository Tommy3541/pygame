import pygame
from utility import image_cutter
from settings import *

class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, direction):
        super().__init__()
        self.x = x
        self.y = y
        self.speed = speed

        self.idle = pygame.image.load(f'assets/sprites/monster/monster2.png').convert_alpha()
        self.idle = pygame.transform.scale(self.idle, (self.idle.get_width()*6, self.idle.get_height()*6))

        self.run1 = pygame.image.load(f'assets/sprites/monster/monster2_2.png').convert_alpha()
        self.run1 = pygame.transform.scale(self.run1, (self.run1.get_width()*6, self.run1.get_height()*6))

        self.run2 = pygame.image.load(f"assets/sprites/monster/monster2_3.png").convert_alpha()
        self.run2 = pygame.transform.scale(self.run2, (self.run2.get_width()*6, self.run2.get_height()*6))

        self.direction = direction

        self.images = [self.idle, self.run1, self.run2]
        self.index = 0
        self.surf = self.images[self.index]
        self.rect = self.surf.get_rect(midbottom=(self.x, self.y))

    def animation(self):
        self.index += 0.1
        if self.index > len(self.images):
            self.index = 0
        self.surf = self.images[int(self.index)]
    
    def update(self):
        if self.direction == "horizontal":
            self.rect.x += self.speed

            if self.rect.right >= SCREEN_WIDTH:
                self.speed *= -1
            elif self.rect.left <= 0:
                self.speed *= -1

        elif self.direction == "vertical":
            self.rect.y += self.speed

            if self.rect.bottom >= SCREEN_HEIGHT:
                self.speed *= -1
            elif self.rect.top <= 0:
                self.speed *= -1
        
        else:
            print("wrong direction")

        self.animation()

    def draw(self, screen):
        screen.blit(self.surf, self.rect)

class Monster2(Monster):
    def __init__(self, x, y, direction, speed=3):
        super().__init__(x, y, speed, direction)
        self.spritesheet = pygame.image.load("assets/sprites/player/woman_blonde_run.png").convert_alpha()
        self.image = image_cutter(self.spritesheet, 0, 0, 15, 16, 3)
        self.rect = self.image.get_rect(midbottom=(self.x, self.y))
    
    def animation(self):
        frame_count = 3

        self.index += 0.1

        if self.index >= frame_count:
            self.index = 0

        self.image = image_cutter(self.spritesheet, int(self.index), 0, 15, 16, 3)

    def scream(self):
        print("AAAAA")
    
    def update(self):
        super().update()
        self.scream()