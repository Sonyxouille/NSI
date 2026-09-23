import pyxel

class Personnage:
    def __init__(self) -> None:
        self.xp = 0
        self.y = 0

    def movement(self,xp):
        if pyxel.btn(pyxel.KEY_D):
            self.xp += 1

    def update(self):
        self.movement(self)

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.xp, 0, 8, 8, 9)

class App:
    def __init__(self):
        pyxel.init(128, 128, title="Nuit du Code")
        self.x = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        Personnage()
        self.x = (self.x + 1) % pyxel.width

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x, 0, 8, 8, 9)

App()