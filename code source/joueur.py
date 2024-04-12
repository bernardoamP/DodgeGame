"""
@file joueur.py
@brief Ce fichier contient la classe Player qui représente le personnage contrôlé par le joueur.

@details
- La classe Player gère les actions du joueur telles que le mouvement, les attaques et les dégâts subis.
- Elle contrôle également la barre de vie du joueur et l'affichage à l'écran.
"""

import pygame
from boule import Boule

pygame.init()

class Player(pygame.sprite.Sprite):
    """
    @brief Classe représentant le personnage contrôlé par le joueur.

    @details
    - Le joueur a une quantité de points de vie, une vitesse de déplacement et une attaque définis.
    - Il peut lancer des boules pour attaquer les ennemis.
    - Sa position et sa barre de vie sont gérées par cette classe.
    """

    def __init__(self, game):
        """
        @brief Initialise les attributs du joueur.

        @param game: Instance de la classe Game à laquelle le joueur appartient.
        """

        super().__init__()
        self.game = game
        self.hp = 100
        self.max_hp = 100
        self.attack = 10
        self.vitesse = 5
        self.all_boule = pygame.sprite.Group()
        self.image = pygame.image.load('assets/G1.png',)
        self.image = pygame.transform.scale(self.image, (300, 300))
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 450

    def damage(self, amount):
        """
        @brief Inflige des dégâts au joueur.

        @param amount: Montant des dégâts à infliger.
        """

        if self.hp - amount > amount:
            self.hp -= amount
        else:
            self.game.game_over()

    def update_hp_bar(self, surface):
        """
        @brief Met à jour la barre de vie du joueur et l'affiche à l'écran.

        @param surface: Surface de l'écran du jeu où afficher la barre de vie.
        """

        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 50, self.rect.y + 20, self.max_hp, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 50, self.rect.y + 20, self.hp, 5])

    def reset_health(self):
        """
        Réinitialise les points de vie du joueur à leur valeur maximale.
        """
        self.hp = self.max_hp

    def lance_boule(self):
        """
        @brief Lance une boule depuis le joueur.
        """

        self.all_boule.add(Boule(self))

    def move_right(self):
        """
        @brief Déplace le joueur vers la droite.

        @details
        - Vérifie s'il y a une collision avec les ennemis avant de déplacer le joueur.
        """

        if not self.game.check_collision(self, self.game.all_enemy):
            self.rect.x += self.vitesse

    def move_left(self):
        """
        @brief Déplace le joueur vers la gauche.
        """

        self.rect.x -= self.vitesse
