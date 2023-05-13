import pygame

class Object:
    objects = []

    def __init__(self, size, color, rect):
        self.size = size
        self.color = color
        self.rect = rect
        Object.objects.append(self)

    # Function that draws a given object on the screen
    def draw(self, screen):
        return pygame.draw.rect(screen, self.color, self.rect, self.size)

    # Function that checks if an object has been clicked
    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)