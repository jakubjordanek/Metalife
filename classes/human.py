from object import Object
from db import connect_db
import pygame
import math

class Human(Object):
    def __init__(self, size, rect, gender, hunger):
        super().__init__(size, (232, 190, 172), rect)
        self.gender = gender
        self.hunger = hunger

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

humans_list = []           

def create_human(size, x, y, gender, hunger):
    rect = pygame.Rect(x, y, size, size)
    human = Human(size, rect, gender, hunger)
    humans_list.append(human)

def generate_humans():
    for human in load_humans():
        create_human(human[1], human[2], human[3], human[4], human[5])

def load_humans():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM humans")
    return cursor.fetchall()
    db.close()

generate_humans()