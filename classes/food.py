from object import Object

class Food(Object):
    def __init__(self, color, rect, hunger):
        super().__init__(color, rect)
        self.hunger = hunger