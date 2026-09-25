import pyxel

class Ennemi:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vitesse = 1

    def update(self):
        self.x = (self.x + self.vitesse) % pyxel.width

    def draw(self):
        pyxel.rect(self.x, self.y, 8, 8, 8)

class Game:
    def __init__(self):
        pyxel.init(160, 120)
        self.ennemis = [Ennemi(10, 10), Ennemi(50, 30)]
        pyxel.run(self.update, self.draw)

    def update(self):
        for e in self.ennemis:
            e.update()

    def draw(self):
        pyxel.cls(0)
        for e in self.ennemis:
            e.draw()

Game()