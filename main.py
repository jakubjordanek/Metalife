import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

import sys
sys.path.append("classes")

import pygame
from display import WIDTH, HEIGHT
from event import events_list
from human import humans_list
from food import food_list

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption("Metalife")
pygame.time.set_timer(pygame.USEREVENT, 5000)
    
running = True
while running:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
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
                        # human.hunger += (target.size * 0.1)
                        human.hunger += target.hunger
                        food_list.remove(target)
        human.draw(screen)

    for food in food_list:
        food.draw(screen)

    pygame.display.update()

pygame.quit()