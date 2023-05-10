from object import Object
from db import connect_db
import pygame

class Food(Object):
    food = []

    def __init__(self, size, rect, hunger):
        super().__init__(size, (184, 48, 48), rect)
        self.hunger = hunger
        Food.food.append(self)

    @classmethod
    def create(cls, size, x, y, hunger):
        rect = pygame.Rect(x, y, size, size)
        cls(size, rect, hunger)

    def delete(self):
        Food.food.remove(self)
        Object.objects.remove(self)

# download and generate food from the database
def generate_food():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM food")
    for food in cursor.fetchall():
        Food.create(food[1], food[2], food[3], food[4])
    db.close()

generate_food()