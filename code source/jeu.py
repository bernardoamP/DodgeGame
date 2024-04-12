"""
@file jeu.py
@brief Ce fichier contient la classe Game qui gère le déroulement du jeu.

@details
- La classe Game initialise et gère les éléments du jeu, tels que les joueurs et les ennemis.
- Elle contrôle le déroulement du jeu, la mise à jour de l'écran et la gestion des collisions.
- Elle gère également le score du joueur et l'enregistrement des scores dans une base de données.
"""

import pygame
import sqlite3
from joueur import Player
from enemy import Enemy
from database_utils import insert_score

# Initialisation de Pygame
pygame.init()


class Game:
    """
    @brief Classe principale du jeu qui gère le déroulement du jeu.

    @details
    - Initialise les paramètres du jeu et les éléments de jeu tels que les joueurs et les ennemis.
    - Gère le déroulement du jeu, la mise à jour de l'écran et la gestion des collisions.
    - Contrôle le score du joueur et l'enregistrement des scores dans une base de données.
    """

    def __init__(self):
        """
        @brief Initialise les paramètres du jeu.
        """

        self.is_playing = False
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.all_enemy = pygame.sprite.Group()
        self.score = 0
        self.pressed = {}

    def start(self):
        """
        @brief Démarre le jeu en initialisant les éléments de jeu.
        """

        self.is_playing = True
        self.spawn_enemy()
        self.spawn_enemy()
        self.spawn_enemy()

    def add_score(self, points=10):
        """
        @brief Ajoute des points au score du joueur.

        @param points: Nombre de points à ajouter au score (par défaut 10).
        """

        self.score += points

    def game_over(self):
        """
        @brief Gère la fin du jeu en réinitialisant les paramètres et en enregistrant le score.
        """

        self.all_enemy = pygame.sprite.Group()
        self.player.healh = self.player.max_hp
        self.is_playing = False
        insert_score("Player", self.score)
        self.score = 0
        self.player.reset_health()

    def update(self, screen):
        """
        @brief Met à jour les éléments du jeu et affiche l'écran de jeu.

        @param screen: Surface de l'écran du jeu.
        """

        font_size = 25
        font = pygame.font.Font("assets/animeace2_reg.ttf", font_size)
        score_text = font.render(f"Score : {self.score}", True, (255, 255, 255))
        screen.blit(score_text, (30, 20))

        screen.blit(self.player.image, self.player.rect)
        self.player.update_hp_bar(screen)

        for boule in self.player.all_boule:
            boule.move()

        for enemy in self.all_enemy:
            enemy.forward()
            enemy.update_hp_bar(screen)

        self.player.all_boule.draw(screen)
        self.all_enemy.draw(screen)

        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self, sprite, group):
        """
        @brief Vérifie les collisions entre un sprite et un groupe de sprites.

        @param sprite: Sprite à vérifier la collision.
        @param group: Groupe de sprites avec lesquels vérifier la collision.

        @return: Liste des sprites en collision avec le sprite spécifié.
        """

        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_enemy(self):
        """
        @brief Génère un ennemi et l'ajoute au groupe d'ennemis.
        """

        enemy = Enemy(self)
        self.all_enemy.add(enemy)
