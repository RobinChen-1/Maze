from GameFrame import Level
from Objects.Character import Character
from Objects.End import End
from Objects.Startflag import Startflag
from Objects.Goldcoin1 import Goldcoin1
from Objects.Goldcoin2 import Goldcoin2
from Objects.Goldcoin3 import Goldcoin3

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