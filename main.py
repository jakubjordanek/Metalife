import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

import pygame
from display import WIDTH, HEIGHT
from human import humans, generate_humans
from food import foods, generate_food

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption("Metalife")
pygame.time.set_timer(pygame.USEREVENT, 5000)

generate_humans(5)
    
running = True
timer = 0

while running:
    dt = clock.tick(60)
    timer += dt

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.USEREVENT:
            for human in humans:
                human.hunger -= 35

    if timer >= 2000:
        generate_food(5)
        timer = 0

    screen.fill((58, 196, 24))

    for human in humans:
        if len(foods) > 0:
            if human.hunger < 70:
                human.find_target(foods)
                for target in foods:
                    if human.rect.colliderect(target.rect):
                        human.hunger += target.hunger
                        foods.remove(target)
        human.draw(screen)

    for food in foods:
        food.draw(screen)

    pygame.display.flip()

pygame.quit()