import pygame

class Object:
    def __init__(self, name, color, rect):
        self.name = name
        self.color = color
        self.rect = rect

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def is_clicked(self, mouse_position):
        return self.rect.collidepoint(mouse_position)