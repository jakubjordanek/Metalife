from object import Object
import math

class Human(Object):
    def __init__(self, color, rect):
        super().__init__(color, rect)
        self.hunger = 100

    def move_to_target(self, target):
        dx = target.rect.x - self.rect.x
        dy = target.rect.y - self.rect.y

        distance = math.sqrt(dx ** 2 + dy ** 2)

        if distance > 0:
            dx /= distance
            dy /= distance

            self.rect.x += int(dx * 5)
            self.rect.y += int(dy * 5)

    def find_closest_target(self, targets):
        nearest_target = None
        min_distance = float("inf")

        for target in targets:
            dx = target.rect.x - self.rect.x
            dy = target.rect.y - self.rect.y
            distance = math.sqrt(dx ** 2 + dy ** 2)

            if distance < min_distance:
                min_distance = distance
                nearest_target = target

        if nearest_target:
            self.move_to_target(nearest_target)