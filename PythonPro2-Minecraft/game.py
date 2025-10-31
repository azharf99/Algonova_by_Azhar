from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager
from hero import Hero


class Game(ShowBase):
   def __init__(self):
       ShowBase.__init__(self)
       self.land = Mapmanager(self.loader, self.render)
       x,y = self.land.loadLand("land.txt")
       self.hero = Hero(self, (x//2,y//2,2), self.land, self.loader, self.render)
       self.camLens.setFov(90)


game = Game()
game.run()
