import pyxel
from position_data import initialisation_position
from images_pièces import image_piece
from fonctions_auxiliaires import gestion_commande
from case_en_danger import detection_echec_et_math
side_length = 16
case_per_line = 8

position=initialisation_position()
damier =[]
for i in range (0, case_per_line):
    for j in range (0,case_per_line): 
        if i%2==j%2 : 
            damier.append((i,j))

def color(piece):
    if piece[-1]=="1":
        return 3
    if piece[-1]=="2":
        return 9
    if piece[0]=="2":
        return 11
    if piece[0]=="1" :
        return 15
    
    
class App:
    def __init__(self,start,position):
        self.start=start
        self.couleur_blanche=7
        self.doubleclic=[]
        self.tour_joueur="2"
        self.position=position
        self.echec=[] #((coordonnées du roi en echec) 
        pyxel.init(side_length*case_per_line,side_length*case_per_line, title="Jeu d'échec")
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)

        
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        self.draw_maze()
        self.draw_piece()
        self.detection()
    
    def draw_maze(self):
        for x in range (0, case_per_line):
            for y in range (0,case_per_line): 
                coloration=0
                if x%2==y%2 : 
                    coloration=self.couleur_blanche
                if (x,y) in self.echec : 
                        piece=position[(x,y)]
                        coloration=color(piece[-1]+piece[0:len(piece)-1])
                for i in range (0,side_length) :
                    for j in range (0,side_length):
                        pyxel.pset(side_length*x+i,y*side_length+j,coloration)
            
    def draw_piece(self):
        for x in range (0,case_per_line):
            for y in range (0,case_per_line):
                piece=self.position[(x,y)]
                if piece !=None :
                    coloration=color(piece)
                    name=piece[0:len(piece)-1]
                    for i,j in image_piece[name]:
                        pyxel.pset(side_length*x+i,y*side_length+j,coloration)
    def detection(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) : 
            x = pyxel.mouse_x//16
            y = pyxel.mouse_y//16
            self.doubleclic.append((x,y))
            self.maj()
    
    def maj(self):
        if len(self.doubleclic)==2 and self.doubleclic[1]!=self.doubleclic[0]:
            self.tour_joueur, self.position= gestion_commande(self.position,self.doubleclic[0],self.doubleclic[1], self.tour_joueur)
            self.echec = detection_echec(self.position)
        if len(self.doubleclic)>=2: 
            self.doubleclic=[]
        self.end()
        
    def end(self):
        etat=detection_echec_et_math(self.position) #récupere le roi en echec, ou None. 
        if etat=="roi1" or not "roi1" in self.position.values() : #si le roi1 est "mangé" ou en echec et maths, les cases blanches se colorent en la couleur du joueur 2
            self.couleur_blanche=15
        if etat=="roi2" or not "roi2" in self.position.values() : #si le roi2 est "mangé" ou en echec et maths, les cases blanches se colorent en la couleur du joueur 1
            self.couleur_blanche=11
    
App(damier, position)
