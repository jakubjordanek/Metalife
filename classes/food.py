from object import Object
from db import connect_db
import pygame

class Food(Object):
    def __init__(self, size, rect, hunger):
        super().__init__(size, (184, 48, 48), rect)
        self.hunger = hunger

def load_food():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM food")
    return cursor.fetchall()
    db.close()

def generate_food():
    food_list = []
    for i in load_food():
        size = i[1]
        x = i[2]
        y = i[3]
        hunger = i[4]
        rect = pygame.Rect(x, y, size, size)
        food = Food(size, rect, hunger)
        food_list.append(food)
    return food_list