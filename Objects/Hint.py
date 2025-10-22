from GameFrame import RoomObject
import pygame

class Hint(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        image = self.load_image("Hint.png")
        self.set_image(image, 202, 101)
