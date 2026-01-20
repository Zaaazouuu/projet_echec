import pyxel
from position_data import initialisation_position
from images_pièces import image_piece
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
print(position)

class App:
    def __init__(self,start):
        self.start=start
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
    
    def draw_maze(self):
        for x,y in self.start :
            for i in range (0,side_length) :
                for j in range (0,side_length):
                    pyxel.pset(side_length*x+i,y*side_length+j,7)
            
    def draw_piece(self):
        for x in range (0,case_per_line):
            for y in range (0,case_per_line):
                piece=position[(x,y)]
                if piece !=None :
                    coloration=color(piece)
                    name=piece[0:len(piece)-1]
                    for i,j in image_piece[name]:
                        pyxel.pset(side_length*x+i,y*side_length+j,coloration)       
App(damier)