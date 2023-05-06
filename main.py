import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

import sys
sys.path.append("classes")

import pygame
import random
from display import WIDTH, HEIGHT
from human import Human
from food import Food

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption("Metalife")
pygame.time.set_timer(pygame.USEREVENT, 5000)

objects_list = []

humans_list = []
for i in range(5):
    color = (232, 190, 172)
    rect = pygame.Rect(random.randint(0, WIDTH - 20), random.randint(0, HEIGHT - 20), 20, 20)
    human = Human(color, rect)
    humans_list.append(human)
    objects_list.append(human)

food_list = []
for i in range(15):
    color = (184, 48, 48)
    rect = pygame.Rect(random.randint(0, WIDTH - 20), random.randint(0, HEIGHT - 20), 10, 10)
    hunger = 20
    food = Food(color, rect, hunger)
    food_list.append(food)
    objects_list.append(food)
    
running = True
while running:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for object in objects_list:
                if object.is_clicked(mouse_pos):
                    print(object.__class__.__name__ + ", Hunger: " + str(object.hunger))
        elif event.type == pygame.USEREVENT:
            for human in humans_list:
                human.hunger -= 35

    screen.fill((58, 196, 24))

    for human in humans_list:
        if len(food_list) > 0:
            if human.hunger < 70:
                human.find_closest_target(food_list)
                for target in food_list:
                    if human.rect.colliderect(target.rect):
                        human.hunger += target.hunger
                        food_list.remove(target)
                        objects_list.remove(target)

    for object in objects_list:
        object.draw(screen)

    pygame.display.update()

pygame.quit()