import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

import sys
sys.path.append("classes")

import pygame
import random
from display import WIDTH, HEIGHT, FPS
from event import Event
from object import Object
from human import Human
from food import Food, create_food

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption("Metalife")

Event(2000, lambda: create_food(10, random.randint(0, WIDTH - 10), random.randint(0, HEIGHT - 10), 20))
Event(5000, lambda: Human.take_hunger())

running = True
while running:
    dt = clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = pygame.time.get_ticks()
    
    for event in Event.events:
        if current_time - event.time >= event.delay:
            event.function()
            event.time = current_time

    screen.fill((58, 196, 24))

    for human in Human.humans:
        if len(Food.food) > 0:
            if human.hunger < 70:
                human.find_closest_target(Food.food)
                for target in Food.food:
                    if human.rect.colliderect(target.rect):
                        human.hunger += target.hunger
                        Food.food.remove(target)
                        Object.objects.remove(target)

    for object in Object.objects:
        object.draw(screen)

    pygame.display.update()

pygame.quit()