from object import Object
from db import connect_db
import pygame

class Food(Object):
    def __init__(self, size, rect, hunger):
        super().__init__(size, (184, 48, 48), rect)
        self.hunger = hunger

food_list = []

def create_food(size, x, y, hunger):
    rect = pygame.Rect(x, y, size, size)
    food = Food(size, rect, hunger)
    food_list.append(food)

def generate_food():
    for food in load_food():
        create_food(food[1], food[2], food[3], food[4])

def load_food():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM food")
    return cursor.fetchall()
    db.close()

generate_food()