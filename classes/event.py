from display import WIDTH, HEIGHT
from human import Human
from food import Food
import pygame
import random

class Event:
    events = []

    def __init__(self, delay, function):
        self.delay = delay
        self.time = pygame.time.get_ticks()
        self.function = function
        Event.events.append(self)

    # Function that supports the creation of a new 'Event'
    @classmethod
    def create(cls, delay, function):
        cls(delay, function)

# Event to increase the level of human hunger
Event.create(10 * 1000, lambda: Human.increase_hunger(40))

# Event creating food
Event.create(2 * 1000, lambda: Food.create(10, random.randint(0, WIDTH - 10), random.randint(0, HEIGHT - 10), 40))