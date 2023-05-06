import pygame

class Object:
    def __init__(self, color, rect):
        self.color = color
        self.rect = rect

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)