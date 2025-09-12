from GameFrame import Level

class EndRoom(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        self.set_background_image("EndRoom_background.png")
