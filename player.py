from datetime import time

import pygame
import animation

class Player(animation.AnimateSprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 1
        self.image = pygame.image.load('assets/ryu/frame_0_delay-0.09s.gif')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 50 # from up

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def update_animation(self):
        self.animate()
