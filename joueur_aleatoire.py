
import random as rd

def joueur_aleatoire(position):
    pieces_j2 = []
    for case, piece in position.items():
        if piece is not None and piece[-1]=="2":
            pieces_j2.append(case)
    while True:
        depart = rd.choice(pieces_j2)
        
        arrivee = (rd.randint(0, 7), rd.randint(0, 7))
        copie_position = position.copy()
        nouvelle_position = gestion_commande(copie_position, depart, arrivee)

       
        if nouvelle_position != position:
            return nouvelle_position





