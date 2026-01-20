import pyxel
from position_data import initialisation_position
from images_pieces import image_piece
side_length = 16
case_per_line = 8

position_initiale=initialisation_position()
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


class App:
    def __init__(self,start):
        self.start=start
        pyxel.init(side_length*case_per_line,side_length*case_per_line, title="Jeu d'échec")
        pyxel.run(self.update, self.draw)
        

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        self.draw_maze()
    
    def draw_maze(self):
        for x,y in self.start :
            for i in range (0,side_length) :
                for j in range (0,side_length):
                    pyxel.pset(side_length*x+i,y*side_length+j,7)
            piece=position_initiale(x,y)
            if piece !=None :
                coloration=color(piece)
                for i,j in image_piece(piece[0:len(piece)-1]):
                    pyxel.pset(side_length*x+i,y*side_length+j,coloration)       
App(damier,image_piece)