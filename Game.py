import Defines
import Element
import Snake
import Boarder

import time

from sense_hat import SenseHat

consol_output = [[0] * Defines.geometry[1] for _ in range(Defines.geometry[0])]

sense = SenseHat()
snake1 = Snake.Snake([3,3], 3, Defines.right)
boarder = Boarder.Boarder([Defines.geometry[Defines.x], Defines.geometry[Defines.y]])

def clear_all():
    for y in range(Defines.geometry[Defines.y]):
        for x in range(Defines.geometry[Defines.x]):
            sense.set_pixel(x, y, 0, 0, 0)

def clear_game():
    snake1.print_snake(" ", sense)


def print_game():
    snake1.print_snake("X", sense)
    boarder.print_boarder(sense)
    time.sleep(1)

clear_all()


clear_game()
snake1.move_snake(Defines.left)
print_game()

clear_game()
snake1.move_snake(Defines.left)
print_game()

clear_game()
snake1.move_snake(Defines.up)
print_game()

clear_game()
snake1.move_snake(Defines.up)
print_game()

clear_game()
snake1.move_snake(Defines.right)
print_game()

clear_game()
snake1.move_snake(Defines.right)
print_game()

clear_game()
snake1.move_snake(Defines.right)
print_game()

clear_game()
snake1.move_snake(Defines.right)
print_game()
#snake1.move_snake(Defines.right)
#snake1.move_snake(Defines.right)
#snake1.move_snake(Defines.right)
#snake1.move_snake(Defines.right)