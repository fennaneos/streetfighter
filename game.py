from player import Player

class Game:
    def __init__(self):
        self.player = Player()
        self.pressed = {
        }

    def update_screen(self, screen):
        screen.blit(self.player.image, self.player.rect)
        self.player.update_animation()