import pygame
from GameFrame import RoomObject, Level


class TextObject(RoomObject):
    """
    A drawable text object for displaying text in a game level.

    Inherits from RoomObject and provides functionality for rendering and updating text
    with customizable font, size, color, and style.

    Attributes:
        rendered_text: The rendered pygame Surface of the text.
        rect (pygame.Rect): The rectangle representing the text's position and size.
        built_font: The pygame Font object used for rendering.
        text (str): The text string to display.
        size (int): Font size.
        font (str): Font name.
        colour (tuple): RGB color of the text.
        bold (bool): Whether the font is bold.
    """

    def __init__(self, room: Level, x: int, y: int, text='Not Set', size=60,
                 font='Comic Sans MS', colour=(0, 0, 0), bold=False):
        """
        Initializes a TextObject with the given properties.

        Args:
            room (Level): The game level or room where the object is placed.
            x (int): The x-coordinate of the object.
            y (int): The y-coordinate of the object.
            text (str, optional): The text to display. Defaults to 'Not Set'.
            size (int, optional): Font size. Defaults to 60.
            font (str, optional): Font name. Defaults to 'Comic Sans MS'.
            colour (tuple, optional): RGB color of the text. Defaults to (0, 0, 0).
            bold (bool, optional): Whether the font is bold. Defaults to False.
        """
        RoomObject.__init__(self, room, x, y)

        self.rendered_text = 0
        self.rect = 0
        self.built_font = 0
        self.text = text
        self.size = size
        self.font = font
        self.colour = colour
        self.bold = bold
        self.update_text()

    def update_text(self):
        """
        Updates the rendered text surface and its rectangle based on current properties.
        """
        self.built_font = pygame.font.SysFont(self.font, self.size, self.bold)
        self.rendered_text = self.built_font.render(self.text, False, self.colour)
        self.image = self.rendered_text
        self.width, self.height = self.built_font.size(self.text)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
