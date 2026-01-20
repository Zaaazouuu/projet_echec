from main import case_per_line

pions_sépciaux_joueur1=["tour1","cavalier1","fou1","dame1","roi1","fou1","cavalier1","tour1"]
pions_sépciaux_joueur2=["tour2","cavalier2","fou2","dame2","roi2","fou2","cavalier2","tour2"]

def initialisation_position():
    positions_initiale = {}
    for j in range (2, case_per_line-2):
        for i in range (0,case_per_line): 
            positions_initiale[(i,j)]="None"
    for i in range (0,case_per_line): 
        positions_initiale[(i,1)]="pion1"
        positions_initiale[(i,0)]=pions_sépciaux_joueur1[i]
        positions_initiale[(i,case_per_line-1)]="pion2"
        positions_initiale[(i,case_per_line)]=pions_sépciaux_joueur2[i]
    return positions_initiale

        



