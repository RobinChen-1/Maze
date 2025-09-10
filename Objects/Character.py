from GameFrame import RoomObject, Globals
import pygame

class Character(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        image = self.load_image("Character_right.png")
        self.set_image(image,64,64)
        self.handle_key_events = True

    def key_pressed(self, key):
        if key[pygame.K_w]:
            self.y -= 8
            image = self.load_image("Character_forward.png")
            self.set_image(image,64,64)
        elif key[pygame.K_s]:
            self.y += 8
            image = self.load_image("Character_back.png")
            self.set_image(image,64,64)
        elif key[pygame.K_a]:
            self.x -= 8
            image = self.load_image("Character_left.png")
            self.set_image(image,64,64)
        elif key[pygame.K_d]:
            self.x += 8
            image = self.load_image("Character_right.png")
            self.set_image(image,64,64)

    def keep_in_room(self):
        if self.y < 0:
            self.y = 0
        elif self.y + self.height> Globals.SCREEN_HEIGHT:
            self.y = Globals.SCREEN_HEIGHT - self.height
        if self.x < 0:
            self.x = 0
        elif self.y + self.width> Globals.SCREEN_WIDTH:
            self.y = Globals.SCREEN_WIDTH - self.width
            
    def step(self):
        self.keep_in_room()