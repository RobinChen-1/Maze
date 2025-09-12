from GameFrame import RoomObject
import pygame

class End(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        image = self.load_image("End.png")
        self.set_image(image, 64, 64)

        self.register_collision_object("Character")

    def handle_collision(self, other, other_type):
        if other_type == "Character":
            self.room.running = False