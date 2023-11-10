from datetime import time

import pygame

from game import Game

pygame.init()

# Music
pygame.mixer.init()
pygame.mixer.music.load("assets/sounds/Ryu_music.mp3")
pygame.mixer.music.play(loops=0)

background = pygame.image.load('assets/StreetFighterBg.gif')

game = Game()

pygame.display.set_caption("Street Fighter Game")

width, height = 1280, 540
screen = pygame.display.set_mode((width, height))

running = True

while running:

    screen.blit(background, (0, 0))
    game.update_screen(screen)

    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    if game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.K_SPACE:
            game.player.image = pygame.image.load('assets/Ryu_kick.gif')
            screen.blit(game.player.image, game.player.rect)

        # detect in realtime if key is being pressed by user
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

