import time

import pygame

class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/ryu/frame_0_delay-0.09s.gif')
        self.current_sprite_num = 0
        self.images = animations.get("ryu")

    def animate(self):
        self.current_sprite_num += 1

        if self.current_sprite_num >= len(self.images):
            self.current_sprite_num = 0

        self.image = self.images[self.current_sprite_num]
        time.sleep(0.05)

def load_animation_images():
    images = []
    for num in range(6):
        images.append(pygame.image.load(f'assets/ryu/frame_{num}_delay-0.09s.gif'))
    return images

animations = {
    'ryu': load_animation_images()
}

