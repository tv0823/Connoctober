import pygame
from constants import *

class Button:
    pygame.font.init()

    def __init__(self, x_pos, y_pos, width, height, text, color=BTN_COLOR, text_color=BROWN):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.text_color = text_color
        self.font = pygame.font.Font(None, 30)

    def draw(self, screen):
        # Draws the button with text on the screen
        pygame.draw.rect(screen, self.color, (self.x_pos, self.y_pos, self.width, self.height), border_radius=5)

        # Render text
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=(self.x_pos + self.width // 2, self.y_pos + self.height // 2))

        # Draw text on the button
        screen.blit(text_surface, text_rect)
