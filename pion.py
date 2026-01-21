if nom_piece == "pion":
        dx = vecteur_deplacement[0]
        dy = vecteur_deplacement[1]
        
        if dx == 0: 
            if pos_arrivee in position:
                return False

            if fa.mvt_pion(vecteur_deplacement, joueur):
                position[pos_arrivee]=piece
                position[pos_depart]=None
                return position
            
            if fa.mvt_initial_pion(vecteur_deplacement, joueur):
                if fa.chemin_libre(pos_depart, pos_arrivee, position):
                    position[pos_arrivee]=piece
                    position[pos_depart]=None
                    return position
                
            return False

        elif abs(dx) == 1 and abs(dy) == 1:
            if pos_arrivee in position:               
                if (joueur == "1" and dy == -1) or (joueur == "2" and dy == 1):
                    position[pos_arrivee]=piece
                    position[pos_depart]=None
                    return position
        

        return False