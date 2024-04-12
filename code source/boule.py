"""
@file boule.py
@brief Ce fichier contient la classe Boule qui représente les projectiles lancés par le joueur.

@details
- La classe Boule gère le mouvement, la rotation et la collision des projectiles.
"""

import pygame

class Boule(pygame.sprite.Sprite):
    """
    @brief Classe représentant les projectiles lancés par le joueur.

    @details
    - Les projectiles ont une vitesse, une image et une position définies.
    - Ils peuvent se déplacer, tourner et détecter les collisions avec les ennemis.
    """

    def __init__(self, player):
        """
        @brief Initialise les attributs du projectile.

        @param player: Instance de la classe Player qui a lancé le projectile.
        """

        super().__init__()
        self.vitesse = 10
        self.player = player
        self.image = pygame.image.load('assets/balle.png.png')
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 160
        self.rect.y = player.rect.y + 90
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        """
        @brief Fait tourner l'image du projectile.

        @details
        - Incrémente l'angle de rotation et applique la transformation à l'image du projectile.
        - Recentre le rectangle du projectile après la rotation.
        """

        self.angle += 10
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        """
        @brief Supprime le projectile du groupe de projectiles du joueur.
        """

        self.player.all_boule.remove(self)

    def move(self):
        """
        @brief Déplace le projectile et gère les collisions avec les ennemis.

        @details
        - Déplace le projectile vers la droite à une vitesse donnée.
        - Fait tourner le projectile pendant son déplacement.
        - Supprime le projectile en cas de collision avec un ennemi ou s'il dépasse les limites de l'écran.
        """

        self.rect.x += self.vitesse
        self.rotate()

        for enemy in self.player.game.check_collision(self, self.player.game.all_enemy):
            self.remove()
            enemy.damage(self.player.attack)

        if self.rect.x > 1920:
            self.remove()
