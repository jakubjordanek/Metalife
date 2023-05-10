import pygame

class Object:
    objects = []

    def __init__(self, size, color, rect):
        self.size = size
        self.color = color
        self.rect = rect
        Object.objects.append(self)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, self.size)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)