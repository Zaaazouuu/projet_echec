

def case_en_danger(position):
    pieces_j1 = []
    pieces_j2 = []
    for case, piece in position.items():
        if piece is not None:
            if piece[-1] == "1":
                pieces_j1.append((case, piece))
            elif piece[-1] == "2":
                pieces_j2.append((case, piece))
    cases_menacees_1 = set()
    cases_menacees_2 = set()

    for case, piece in pieces_j1:
        if piece is not "pion1":
            for i in range(8):
                for j in range(8):
                   copie_position = position.copy()
                   nouvelle_position = gestion_commande(copie_position, case, (i, j))
                   if nouvelle_position != position:
                        cases_menacees_1.add((i, j))
        else : 
            cases_menacees_1.add((case[0]-1,case[1]+1))
            cases_menacees_1.add((case[0]+1,case[1]+1))

    for case, piece in pieces_j2:
        if piece is not "pion2":
            for i in range(8):
                for j in range(8):
                    copie_position = position.copy()
                    nouvelle_position = gestion_commande(copie_position, case, (i, j))
                    if nouvelle_position != position:
                        cases_menacees_2.add((i, j))
        else :
            cases_menacees_2.add((case[0]-1,case[1]-1))
            cases_menacees_2.add((case[0]+1,case[1]-1))

    return cases_menacees_1, cases_menacees_2
        
        

