from GameFrame import RoomObject
import pygame

class Startflag(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        image = self.load_image("Startflag.png")
        self.set_image(image, 64, 64)