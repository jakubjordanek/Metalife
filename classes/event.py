import pygame
import random
from human import Human
from food import Food

class Event:
    events = []

    def __init__(self, delay, function):
        self.delay = delay
        self.time = pygame.time.get_ticks()
        self.function = function
        Event.events.append(self)

    @classmethod
    def create(cls, delay, function):
        cls(delay, function)

Event.create(5000, lambda: Human.increase_hunger(35))
Event.create(2000, lambda: Food.create(10, random.randint(0, 790), random.randint(0, 590), 20))