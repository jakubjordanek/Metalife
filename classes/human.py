from display import WIDTH, HEIGHT
from object import Object
from food import Food
import pygame
import random
import math

class Human(Object):
    humans = []

    def __init__(self, size, rect, gender, hunger, happiness):
        super().__init__(size, (232, 190, 172), rect)
        self.gender = gender
        self.hunger = hunger
        self.happiness = happiness
        Human.humans.append(self)

    def move(self):
        direction = random.choice(['up', 'down', 'left', 'right'])
        if direction == 'up':
            self.rect.y -= 2
        elif direction == 'down':
            self.rect.y += 2
        elif direction == 'left':
            self.rect.x -= 2
        elif direction == 'right':
            self.rect.x += 2

    def move_to_target(self, target):
        dx = target.x - self.rect.x
        dy = target.y - self.rect.y

        distance = math.sqrt(dx ** 2 + dy ** 2)

        if distance > 0:
            dx /= distance
            dy /= distance

            self.rect.x += int(dx * 5)
            self.rect.y += int(dy * 5)

    def find_closest_target(self, targets):
        nearest_target = None
        min_distance = float("inf")

        for target in targets:
            dx = target.rect.x - self.rect.x
            dy = target.rect.y - self.rect.y
            distance = math.sqrt(dx ** 2 + dy ** 2)

            if distance < min_distance:
                min_distance = distance
                nearest_target = target

        if nearest_target:
            self.move_to_target(nearest_target.rect)

    @classmethod
    def is_hungry(cls):
        for human in cls.humans:
            if human.hunger > 30:
                human.find_closest_target(Food.food)
                for food in Food.food:
                    if human.rect.colliderect(food.rect):
                        human.consume_food(food.hunger)
                        Food.delete(food)

    @classmethod
    def increase_hunger(cls, hunger):
        for human in cls.humans:
            human.hunger += hunger

    def consume_food(self, hunger):
        self.hunger -= hunger
        self.increase_happiness(30)
        if self.hunger < 0:
            self.hunger = 0

    def increase_happiness(self, happiness):
        self.happiness += happiness

    @classmethod
    def create(cls, size, x, y, gender, hunger, happiness):
        rect = pygame.Rect(x, y, size, size)
        cls(size, rect, gender, hunger, happiness)

    def delete(self):
        Human.humans.remove(self)
        Object.objects.remove(self)

# generate humans in random position
def generate_humans(COUNT):
    for human in range(COUNT):
        gender = random.choice(['Male', 'Female'])
        size = 20 if gender == 'Male' else 15
        x = random.randint(0, WIDTH - size)
        y = random.randint(0, HEIGHT - size)
        Human.create(size, x, y, gender, 0, 50)

generate_humans(5)