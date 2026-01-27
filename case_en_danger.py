from fonctions_auxiliaires import gestion_commande

def cases_en_danger(position):
    pieces_j1 = []
    pieces_j2 = []
    position_roi1=None
    position_roi2=None
    for case, piece in position.items():
        if piece is not None:
            if piece[-1] == "1":
                pieces_j1.append((case, piece))
                if piece =="roi1" :
                    position_roi1=case 
                    
            elif piece[-1] == "2":
                pieces_j2.append((case, piece))
                if piece =="roi2" :
                    position_roi2=case
    cases_menacees_1 = set()
    cases_menacees_2 = set()

    for case, piece in pieces_j1:
        if piece !="pion1":
            for i in range(8):
                for j in range(8):
                   copie_position = position.copy()
                   nouvelle_position = gestion_commande(copie_position, case, (i, j),"1")[1]
                   if nouvelle_position != position:
                        cases_menacees_1.add((i, j))
        else : 
            cases_menacees_1.add((case[0]-1,case[1]-1))
            cases_menacees_1.add((case[0]+1,case[1]-1))

    for case, piece in pieces_j2:
        if piece !="pion2":
            for i in range(8):
                for j in range(8):
                    copie_position = position.copy()
                    nouvelle_position = gestion_commande(copie_position, case, (i, j),"2")[1]
                    if nouvelle_position != position:
                        cases_menacees_2.add((i, j))
        else :
            cases_menacees_2.add((case[0]-1,case[1]+1))
            cases_menacees_2.add((case[0]+1,case[1]+1))
    if position_roi1 in cases_menacees_2  :
        return "roi1"
    if position_roi2 in cases_menacees_1 : 
        return "roi2"
    return None 

def detection_echec(position):
    return []

def detection_echec_et_math(position):
    "renvoie 'roi1' ou 'roi2' si il est en échec et math, et renvoie 'None' si pas d'echec et math"
    return cases_en_danger(position) #temporairement
         

