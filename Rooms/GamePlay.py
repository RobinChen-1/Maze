from GameFrame import Level, Globals
from Objects.Character import Character
from Objects.End import End
from Objects.Startflag import Startflag
from Objects.Goldcoin1 import Goldcoin1
from Objects.Goldcoin2 import Goldcoin2
from Objects.Goldcoin3 import Goldcoin3
from Objects.Hud import Score
from Objects.Hint import Hint

class GamePlay(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        self.set_background_image("Background.png")

        self.add_room_object(Character(self,280,700))

        self.add_room_object(End(self,920,30))

        self.add_room_object(Startflag(self, 280, 700))

        self.add_room_object(Goldcoin1(self, 287, 110))
        self.add_room_object(Goldcoin2(self, 710, 185))
        self.add_room_object(Goldcoin3(self, 923, 415))

        self.add_room_object(Hint(self, 50, 350))

        self.score = Score(self, 
                           Globals.SCREEN_WIDTH/8 - 20, 20, 
                           str(Globals.SCORE))
        self.add_room_object(self.score)