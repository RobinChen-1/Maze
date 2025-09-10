from GameFrame import Level
from Objects.Character import Character

class GamePlay(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        self.set_background_image("Background.png")

        self.add_room_object(Character(self,280,700))