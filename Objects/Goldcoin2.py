from GameFrame import RoomObject
import pygame

class Goldcoin2(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        image = self.load_image("Goldcoin2.png")
        self.set_image(image, 48, 48)

        self.register_collision_object("Character")

    def handle_collision(self, other, other_type):
        if other_type == "Character":
            self.room.delete_object(self)
            self.room.score.update_score(+100)