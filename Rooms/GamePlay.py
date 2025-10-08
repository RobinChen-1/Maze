from GameFrame import Level
from Objects.Character import Character
from Objects.End import End
from Objects.Startflag import Startflag

class GamePlay(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        self.set_background_image("Background.png")

        self.add_room_object(Character(self,280,700))

        self.add_room_object(End(self,920,30))

        self.add_room_object(Startflag(self, 280, 700))