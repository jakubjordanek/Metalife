from display import WIDTH, HEIGHT
from object import Object
import pygame
import random

class Food(Object):
    food = []

    def __init__(self, size, rect, hunger):
        super().__init__(size, (184, 48, 48), rect)
        self.hunger = hunger
        Food.food.append(self)

    # Function that supports the creation of a new 'Food'
    @classmethod
    def create(cls, size, x, y, hunger):
        rect = pygame.Rect(x, y, size, size)
        return cls(size, rect, hunger)

    # Function that removes this 'Food'
    def delete(self):
        Food.food.remove(self)
        Object.objects.remove(self)

# Function that generates food in random position
def generate_food(COUNT):
    for food in range(COUNT):
        size = 10
        x = random.randint(0, WIDTH - size)
        y = random.randint(0, HEIGHT - size)
        Food.create(size, x, y, 20)

generate_food(5)