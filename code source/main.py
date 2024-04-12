"""
@file main.py
@brief Ce script initialise et lance un jeu de dodge en utilisant Pygame.

@details
- Le jeu affiche un écran titre avec un bouton de lecture.
- Une fois que le bouton de lecture est cliqué, le jeu démarre.
- Le joueur peut contrôler un personnage pour esquiver les balles qui tombent depuis le haut de l'écran.
- Le score du joueur augmente à mesure qu'il survit plus longtemps.
"""

import pygame

from jeu import Game
from database_utils import create_score_table

pygame.init()

pygame.display.set_caption("DODGE GAME")
screen = pygame.display.set_mode((1280, 720))

background = pygame.image.load('assets/wallhaven-l358l2.png')

new_width = 1280
new_height = 720

background = pygame.transform.scale(background, (new_width, new_height))

new_width = int(1280 * 1.35)
new_height = int(720 * 1.35)

banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (400, 400))
banner_rect = banner.get_rect()
banner_rect.x = screen.get_width() / 2.8
banner_rect.y = screen.get_width() / 40

quit_button = pygame.image.load('assets/bouton_exit.png')
quit_button = pygame.transform.scale(quit_button, (80, 80))
quit_button_rect = quit_button.get_rect()
quit_button_rect.x = screen.get_width() - quit_button.get_width() - 10
quit_button_rect.y = screen.get_width() / 140

play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = screen.get_width() / 2.88
play_button_rect.y = screen.get_width() / 3.2

clock = pygame.time.Clock()
FPS = 24

create_score_table()

game = Game()

running = True

while running:

    """
    @brief Boucle principale du jeu.

    @details
    - Met à jour l'écran avec l'arrière-plan et les éléments du jeu.
    - Gère l'entrée utilisateur pour contrôler le jeu.
    """

    screen.blit(background, (0, 0))

    if game.is_playing:
        game.update(screen)
    else:
        screen.blit(quit_button, quit_button_rect)
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Game Close")
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                game.player.lance_boule()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.start()
            elif quit_button_rect.collidepoint(event.pos):
                running = False

clock.tick(FPS)
