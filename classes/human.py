from object import Object
from db import connect_db
import pygame
import math

class Human(Object):
    humans = []

    def __init__(self, size, rect, gender, hunger):
        super().__init__(size, (232, 190, 172), rect)
        self.gender = gender
        self.hunger = hunger
        Human.humans.append(self)

    def move_to_target(self, target):
        dx = target.rect.x - self.rect.x
        dy = target.rect.y - self.rect.y

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
            self.move_to_target(nearest_target)

    @classmethod
    def increase_hunger(cls, hunger):
        for human in cls.humans:
            human.hunger += hunger

    def consume_food(self, hunger):
        self.hunger -= hunger
        if self.hunger < 0:
            self.hunger = 0

    @classmethod
    def create(cls, size, x, y, gender, hunger):
        rect = pygame.Rect(x, y, size, size)
        cls(size, rect, gender, hunger)

    def delete(self):
        Human.humans.remove(self)
        Object.objects.remove(self)

# download and generate people from the database
def generate_humans():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM humans")
    for human in cursor.fetchall():
        Human.create(human[1], human[2], human[3], human[4], human[5])
    db.close()

generate_humans()