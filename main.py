import pyxel

side_length =8

damier = []
for i in range (0, side_length):
    for j in range (0,side_length): 
        if i%2==j%2 : 
            damier.append((i,j))


class App:
    def __init__(self,start):
        self.start=start
        pyxel.init(side_length,side_length, title="Jeu d'échec")
        pyxel.run(self.update, self.draw)
        

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        self.draw_maze()
    
    def draw_maze(self):
        for x,y in self.start :
            pyxel.pset(x,y,7)

App(damier)