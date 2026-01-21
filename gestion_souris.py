#fonction qui a partir d'un premier clic valide (voir dictionnaire) va verfier si le deuxieme clic est un coup valide
import fonctions_auxiliaires as fa


def gestion_souris(position,clic1,clic2):
    pos_depart=clic1
    pos_arrivee=clic2
    piece=position[pos_depart]
    joueur=piece[-1]
    vecteur_deplacement=(pos_arrivee[0]-pos_depart[0],pos_arrivee[1]-pos_depart[1])
    position_finale=fa.position_finale(vecteur_deplacement,pos_depart)
    
    if not fa.dans_le_damier(position_finale):
        return False

    if not fa.non_tir_ami (pos_arrivee,pos_depart,position):
        return False

    nom_piece=piece[0:len(piece)-1]
    
    if nom_piece=="pion":
        if (fa.mvt_initial_pion(vecteur_deplacement,joueur) and 
            ((joueur=="1" and pos_depart[1]==1) or (joueur=="2" and pos_depart[1]==6))) or fa.mvt_pion(vecteur_deplacement,joueur):
            return True
        else:
            return False

    if nom_piece=="cheval":
        return fa.mvt_cheval(vecteur_deplacement)

    if nom_piece=="tour":
        return fa.mvt_tour(vecteur_deplacement)

    if nom_piece=="fou":
        return fa.mvt_fou(vecteur_deplacement)

    if nom_piece=="roi":
        return fa.mvt_roi(vecteur_deplacement)

    if nom_piece=="dame":
        return fa.mvt_reine(vecteur_deplacement)    
    
    return False