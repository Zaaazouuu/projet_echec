import pyxel

# 1. On initialise la fenêtre en premier
# (largeur, hauteur, titre)
pyxel.init(160, 160, title="Mon Jeu d'Échecs")

# 2. Maintenant on peut charger le fichier de ressources
try:
    pyxel.load("image_pièces/res (2).pyxres")
except RuntimeError:
    print("Erreur : Le fichier est introuvable. Vérifiez le nom et le dossier.")

# 3. Fonction de dessin pour afficher une pièce
def draw():
    pyxel.cls(0)
    # Affiche la ressource située en (0,0) dans l'onglet image 0
    # aux coordonnées (10, 10) de l'écran
    pyxel.blt(10, 10, 0, 0, 0, 100, 50)

# 4. On lance le jeu
pyxel.run(lambda: None, draw)