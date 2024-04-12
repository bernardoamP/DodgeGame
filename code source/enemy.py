"""
@file enemy.py
@brief Ce fichier contient la classe Enemy qui représente les ennemis dans le jeu.

@details
- La classe Enemy gère les caractéristiques et le comportement des ennemis.
- Elle gère les dégâts, les points de vie, la vitesse de déplacement et l'apparence des ennemis.
"""

import pygame
import random

class Enemy(pygame.sprite.Sprite):
    """
    @brief Classe représentant les ennemis dans le jeu.

    @details
    - Les ennemis ont des points de vie, des dégâts d'attaque et une vitesse de déplacement aléatoires.
    - Ils se déplacent vers la gauche et infligent des dégâts au joueur s'ils entrent en collision avec lui.
    """

    def __init__(self, game):
        """
        @brief Initialise les attributs de l'ennemi.

        @param game: Instance de la classe Game à laquelle l'ennemi appartient.
        """

        super().__init__()
        self.game = game
        self.hp = 80
        self.max_hp = 80
        self.attack = 0.5
        self.vitesse = random.randint(5, 12)
        self.image = pygame.image.load('assets/e1.png', )
        self.image = pygame.transform.scale(self.image, (200, 300))
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.rect.x = 1500 + random.randint(0, 300)
        self.rect.y = 700

    def damage(self, amount):
        """
        @brief Inflige des dégâts à l'ennemi.

        @param amount: Montant des dégâts à infliger.
        """

        self.hp -= amount

        if self.hp <= 0:
            self.rect.x = 1500 + random.randint(0, 300)
            self.vitesse = random.randint(1, 3)
            self.hp = self.max_hp
            self.game.add_score()

    def update_hp_bar(self, surface):
        """
        @brief Met à jour la barre de vie de l'ennemi et l'affiche à l'écran.

        @param surface: Surface de l'écran du jeu où afficher la barre de vie.
        """

        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_hp, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.hp, 5])

    def forward(self):
        """
        @brief Fait avancer l'ennemi vers la gauche.

        @details
        - Vérifie s'il y a une collision avec le joueur.
        - Inflige des dégâts au joueur s'il y a collision.
        """

        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.vitesse
        else:
            self.game.player.damage(self.attack)
