import pygame

class Event:
    events = []

    def __init__(self, delay, function):
        self.delay = delay
        self.time = pygame.time.get_ticks()
        self.function = function
        Event.events.append(self)