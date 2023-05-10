import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

import sys
sys.path.append("classes")

import pygame
from display import WIDTH, HEIGHT, FPS
from event import Event
from object import Object
from human import Human
from food import Food

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption("Metalife")

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
            if human.hunger > 30:
                human.find_closest_target(Food.food)
                for target in Food.food:
                    if human.rect.colliderect(target.rect):
                        human.consume_food(target.hunger)
                        Food.delete(target)

    for object in Object.objects:
        object.draw(screen)

    pygame.display.update()

pygame.quit()