from src.Patterns.Visitor import Visitable, Visitor
from src.Simulation.Field import Field
from src.Simulation.Snake import Snake, CollisionException
from pygame import Vector2



from src.Simulation.Bonus import Bonus

class Simulation(Visitable):
    def __init__(self, field_size: int, window_size: Vector2):
        self.field = Field(window_size, field_size)
        self.snake = Snake(Vector2(field_size // 2, field_size // 2))
        self.field_size = field_size
        self.last_update = 0
        self.move_interval = 200
        self.current_direction = Vector2(1, 0)
        self.bonus = Bonus(field_size)

    def visit(self, visitor: Visitor):
        visitor.accept(self.field)
        visitor.accept(self.snake)
        visitor.accept(self.bonus)
        
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