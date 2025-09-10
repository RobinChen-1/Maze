from GameFrame import RoomObject
import pygame

class Character(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        image = self.load_image("Character_forward.png")
        self.set_image(image,64,64)
        self.handle_key_events = True

    def key_pressed(self, key):
        if key[pygame.K_w]:
            self.y -= 10
        elif key[pygame.K_s]:
            self.y += 10
        elif key[pygame.K_a]:
            self.x -= 10
        elif key[pygame.K_d]:
            self.x += 10
