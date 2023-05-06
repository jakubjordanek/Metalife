from object import Object
from display import WIDTH, HEIGHT
import pygame
import random

class Food(Object):
    def __init__(self, name, color, rect, hunger):
        super().__init__(name, color, rect)
        self.hunger = hunger

foods = []

def generate_food(COUNT):
    for i in range(COUNT):
        name = "Food"
        color = (184, 48, 48)
        rect = pygame.Rect(random.randint(0, WIDTH - 20), random.randint(0, HEIGHT - 20), 10, 10)
        hunger = 20
        food = Food(name, color, rect, hunger)
        foods.append(food)