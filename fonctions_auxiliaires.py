
#vecteur_deplacement : tuple de déplacement
def position_finale (vecteur_deplacement, position_initiale): 
    position_finale=position_initiale+vecteur_deplacement
    return position_finale

def non_tir_ami(pos_arrivee, pos_depart, position):
    joueur = position[pos_depart][-1]
    if position[pos_arrivee] is not None:
        if position[pos_arrivee][-1] == joueur:
            return False
    return True

def chemin_libre(pos_depart, pos_arrivee, position):
    """
    Vérifie qu'il n'y a aucune pièce entre le départ et l'arrivée.
    Ne vérifie pas la case d'arrivée 
    """
    x1, y1 = pos_depart
    x2, y2 = pos_arrivee
    
    dx = x2 - x1
    dy = y2 - y1
    if dx == 0:
        pas_x = 0
    elif dx > 0:
        pas_x = 1
    else:
        pas_x = -1
    if dy == 0:
        pas_y = 0
    elif dy > 0:
        pas_y = 1
    else:
        pas_y = -1

    x_courant = x1 + pas_x
    y_courant = y1 + pas_y
    while (x_courant, y_courant) != (x2, y2):
        
        if (x_courant, y_courant) in position:
            return False          
        x_courant += pas_x
        y_courant += pas_y
    return True





def dans_le_damier(position_finale):
    if position_finale[0]<16 and position_finale[0]>=0 and position_finale[1]<16 and position_finale[1]>=0 : 
        return True

def mvt_initial_pion(vecteur_deplacement,joueur):
    if joueur == "1":
        if vecteur_deplacement in [(0,1),(0,2)] : 
            return True
    if joueur == "2":
        if vecteur_deplacement in [(0,-1),(0,-2)] : 
            return True
    return False

def mvt_pion(vecteur_deplacement,joueur):
    if joueur == "1":
        if vecteur_deplacement in [(0,1),(1,1),(-1,1)] : 
            return True
    if joueur == "2":
        if vecteur_deplacement in [(0,-1),(-1,-1),(1,-1)] : 
            return True
    return False

def mvt_cheval(vecteur_deplacement):
    print(vecteur_deplacement)
    if vecteur_deplacement in [(2, 1), (2, -1), (-2, 1), (-2, -1),
                             (1, 2), (1, -2), (-1, 2), (-1, -2)]:
        return True
    return False


def mvt_tour(vecteur_deplacement):
    if vecteur_deplacement in ([(0, n) for n in range(-7,8)] + [(n,0) for n in range(-7,8)]):
        return True
    return False


def mvt_fou(vecteur_deplacement):
    if vecteur_deplacement in ([(n, n) for n in range(-7,8)] + [(n, -n) for n in range(-7,8)]):
        return True
    return False    

def mvt_roi(vecteur_deplacement):
    if vecteur_deplacement in [(-1,-1), (-1,0), (-1,1),
                             (0,-1), (0,1),
                             (1,-1),  (1,0), (1,1)]:
        return True
    return False


def mvt_reine(vecteur_deplacement):
    if mvt_tour(vecteur_deplacement) or mvt_fou(vecteur_deplacement):
        return True
    return False


def gestion_commande(position,clic1,clic2):
    pos_depart=clic1
    pos_arrivee=clic2
    piece=position[pos_depart]
    if pos_depart==None : 
        return position
    joueur=piece[-1]
    vecteur_deplacement=(pos_arrivee[0]-pos_depart[0],pos_arrivee[1]-pos_depart[1])
    position_finale=pos_arrivee
    
    if not dans_le_damier(position_finale):
        return position

    if not non_tir_ami (pos_arrivee,pos_depart,position):
        return position

    nom_piece=piece[0:len(piece)-1]
    
    if nom_piece=="pion":
        if (mvt_initial_pion(vecteur_deplacement,joueur) and 
            ((joueur=="1" and pos_depart[1]==1) or (joueur=="2" and pos_depart[1]==6))) or mvt_pion(vecteur_deplacement,joueur) :
            cle=False
            if position[pos_arrivee]==None and vecteur_deplacement in [(0,1),(0,2),(1,0),(2,0),(0,-1),(0,-2),(-1,0),(-2,0)] :
                position[pos_arrivee]=piece
                position[pos_depart]=None
                cle=True
            if position[pos_arrivee]!=None and cle==False and vecteur_deplacement in [(1,1),(-1,-1),(1,-1),(-1,1)]:
                position[pos_arrivee]=piece
                position[pos_depart]=None

    if nom_piece=="cavalier":
        if mvt_cheval(vecteur_deplacement): 
            position[pos_arrivee]=piece
            position[pos_depart]=None


    if nom_piece == "tour":
        if mvt_tour(vecteur_deplacement):
            if chemin_libre(pos_depart, pos_arrivee, position):
                position[pos_arrivee]=piece
                position[pos_depart]=None
        

    if nom_piece=="fou":
        if mvt_fou(vecteur_deplacement):
            if chemin_libre(pos_depart, pos_arrivee, position):
                position[pos_arrivee]=piece
                position[pos_depart]=None

    if nom_piece=="roi":
        if mvt_roi(vecteur_deplacement):
            if chemin_libre(pos_depart, pos_arrivee, position):
                position[pos_arrivee]=piece
                position[pos_depart]=None
        
    if nom_piece=="dame":
        if mvt_reine(vecteur_deplacement):
            if chemin_libre(pos_depart, pos_arrivee, position):
                position[pos_arrivee]=piece
                position[pos_depart]=None
    
    return position


        
   