import Defines
from Element import Element



class Snake:

    def __init__(self, start_pos = [0, 0], len = 0, direction = -1):
        self.snake = []

        if direction == Defines.right:
            for i in range(len):
                start_pos[Defines.x] += 1
                self.add_snake_element(start_pos.copy())
        if direction == Defines.left:
            for i in range(len):
                start_pos[Defines.x] -= 1
                self.add_snake_element(start_pos.copy())



    def add_snake_element(self, pos):
        self.snake.append(Element(pos, Defines.default_rgb))

    def check_collition(self, pos, input_list):
        for i in self.snake:
            if pos == input_list:
                return False
            else:
                return True

    def is_move_valid(self):
        head_pos = self.snake[0].get_pos()

        if self.check_collition(head_pos, self.snake) == False:
            return False
        else:
            return True

    def move_snake(self, direction):
        last_snake_element = self.snake.pop()

        if direction is Defines.up:    
            last_snake_element.set_pos([self.snake[0].get_pos()[Defines.x], self.snake[0].get_pos()[Defines.y] - 1])
        elif direction is Defines.right:
            last_snake_element.set_pos([self.snake[0].get_pos()[Defines.x] + 1, self.snake[0].get_pos()[Defines.y]])
        elif direction is Defines.down:
            last_snake_element.set_pos([self.snake[0].get_pos()[Defines.x], self.snake[0].get_pos()[Defines.y]] + 1)
        elif direction is Defines.left:
            last_snake_element.set_pos([self.snake[0].get_pos()[Defines.x] - 1, self.snake[0].get_pos()[Defines.y]])

        self.snake.insert(0, last_snake_element)

        return self.is_move_valid()
    
    def print_snake(self, c):
        for i in self.snake:
            i.print_element(c)
