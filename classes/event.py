import pygame

class Event(pygame.sprite.Sprite):
    def __init__(self, time, function):
        super().__init__()
        self.time = time
        self.function = function
        self.event = pygame.USEREVENT
        pygame.time.set_timer(self.event, self.time)

    def update(self, *args):
        if args and args[0].type == self.event:
            self.function()

events_list = []

def create_event(time, function):
    event = Event(time, function)
    events_list.append(event)