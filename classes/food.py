from object import Object
from db import connect_db
import pygame

class Food(Object):
    food = []

    def __init__(self, size, rect, hunger):
        super().__init__(size, (184, 48, 48), rect)
        self.hunger = hunger
        Food.food.append(self)

def create_food(size, x, y, hunger):
    rect = pygame.Rect(x, y, size, size)
    Food(size, rect, hunger)

def load_food():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM food")
    for food in cursor.fetchall():
        create_food(food[1], food[2], food[3], food[4])
    db.close()

load_food()