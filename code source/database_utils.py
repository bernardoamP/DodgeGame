"""
@file database_utils.py
@brief Ce fichier contient des fonctions pour gérer une base de données SQLite pour stocker les scores des joueurs.

@details
- Les fonctions permettent de créer une table pour stocker les scores et d'insérer de nouveaux scores dans la base de données.
"""

import sqlite3

def create_score_table():
    """
    @brief Crée la table des scores dans la base de données.

    @details
    - Cette fonction se connecte à la base de données et exécute une requête SQL pour créer la table des scores si elle n'existe pas déjà.
    """

    conn = sqlite3.connect('DodgeGame.db')  # Connexion à la base de données
    c = conn.cursor()
    c.execute('''CREATE TABLE if not exists scores
                 (id INTEGER PRIMARY KEY, player_name TEXT, score INTEGER)''')
    conn.commit()
    conn.close()

def insert_score(player_name, score):
    """
    @brief Insère un nouveau score dans la table des scores.

    @param player_name: Nom du joueur.
    @param score: Score du joueur à insérer.

    @details
    - Cette fonction se connecte à la base de données et insère un nouveau score dans la table des scores avec le nom du joueur et son score.
    """

    conn = sqlite3.connect('DodgeGame.db')
    c = conn.cursor()
    c.execute('''INSERT INTO scores (player_name, score) VALUES (?, ?)''', (player_name, score))
    conn.commit()
    conn.close()
