import pyxel

side_length = 16
case_per_line = 8


damier =[]
for i in range (0, case_per_line):
    for j in range (0,case_per_line): 
        if i%2==j%2 : 
            damier.append((i,j))


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

App(damier)