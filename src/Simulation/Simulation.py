
from src.Simulation.Field import Field
from src.Simulation.Snake import Snake, CollisionException
from pygame import Vector2



from src.Simulation.Bonus import Bonus

class Simulation:
    def __init__(self, field_size: int, window_size: Vector2):
        self.cell_size = Vector2(window_size // field_size)
        self.field = Field(field_size, self.cell_size)
        self.snake = Snake(Vector2(field_size // 2, field_size // 2), self.cell_size)
        self.bonus = Bonus(field_size)
        self.field_size = field_size
        self.last_update = 0
        self.move_interval = 200
        self.current_direction = Vector2(1, 0)

    def draw(self, drawer, font):
        import pygame
        surface = pygame.display.get_surface()
        surface.fill((128, 128, 128))
        drawer.draw_field(self.field.size, self.field.cell_size, font)
        drawer.draw_snake(self.snake.get_segments_with_directions(), self.snake.cell_size)
        drawer.draw_bonus(self.bonus.get_position(), self.field.cell_size)
        
    def update(self, current_time):
        if current_time - self.last_update >= self.move_interval:
            if not self.move_snake(self.current_direction):
                return False
            self.last_update = current_time
        return True
        
    def set_direction(self, direction: Vector2):
        if direction.x != -self.current_direction.x or direction.y != -self.current_direction.y:
            self.current_direction = direction


    def move_snake(self, direction: Vector2):
        try:
            self.snake.move(direction)
            head = self.snake.body[0]
            if not (0 <= head.x < self.field_size and 0 <= head.y < self.field_size):
                return False
            if head == self.bonus.get_position():
                self.snake.grow()
                self.bonus.respawn(self.field_size)
            return True
        except CollisionException:
            return False