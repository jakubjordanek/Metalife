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
        self.interaction = None
        Human.humans.append(self)

    # Function to move 'Human' towards the set interaction target
    def move_to_target(self):
        dx = self.interaction.x - self.rect.x
        dy = self.interaction.y - self.rect.y

        distance = math.sqrt(dx ** 2 + dy ** 2)

        if distance > 0:
            dx /= distance
            dy /= distance

            self.rect.x += int(dx * 5)
            self.rect.y += int(dy * 5)

        if distance < 5:
            self.interaction = None

    # Function that finds the closest object from the given list
    def find_closest_target(self, targets):
        nearest_target = None
        min_distance = float("inf")

        for target in targets:
            if target is not self:
                dx = target.rect.x - self.rect.x
                dy = target.rect.y - self.rect.y
                distance = math.sqrt(dx ** 2 + dy ** 2)

                if distance < min_distance:
                    min_distance = distance
                    nearest_target = target

        if nearest_target:
            return nearest_target.rect

    # Happiness control function for all humans
    @classmethod
    def is_happy(cls):
        for human in cls.humans:
            if human.hunger <= 30:
                if human.interaction is None:
                    human.interaction = pygame.Rect(random.randint(0, WIDTH - human.size), random.randint(0, HEIGHT - human.size), 0, 0)
                human.move_to_target()

    # Hunger control function for all humans
    @classmethod
    def is_hungry(cls):
        for human in cls.humans:
            if human.hunger > 30:
                human.interaction = human.find_closest_target(Food.food)
                human.move_to_target()
                for food in Food.food:
                    if human.rect.colliderect(food.rect):
                        human.consume_food(food.hunger)
                        Food.delete(food)
                
    # Hunger-increasing function for all humans
    @classmethod
    def increase_hunger(cls, hunger):
        for human in cls.humans:
            human.hunger += hunger

    # Function that supports eating food
    def consume_food(self, hunger):
        self.hunger -= hunger
        self.increase_happiness(30)
        if self.hunger < 0:
            self.hunger = 0

    # Happiness-increasing function
    def increase_happiness(self, happiness):
        self.happiness += happiness

    # Function that supports the creation of a new 'Human'
    @classmethod
    def create(cls, size, x, y, gender, hunger, happiness):
        rect = pygame.Rect(x, y, size, size)
        return cls(size, rect, gender, hunger, happiness)

    # Function that removes this 'Human'
    def delete(self):
        Human.humans.remove(self)
        Object.objects.remove(self)

# Function that generates humans in random position
def generate_humans(COUNT):
    for human in range(COUNT):
        gender = random.choice(["Male", "Female"])
        size = 20 if gender == "Male" else 15
        x = random.randint(0, WIDTH - size)
        y = random.randint(0, HEIGHT - size)
        Human.create(size, x, y, gender, 0, 50)

generate_humans(3)