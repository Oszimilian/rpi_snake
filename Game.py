import Defines
import Element
import Snake
import Boarder

import time

consol_output = [[0] * Defines.geometry[1] for _ in range(Defines.geometry[0])]

snake1 = Snake.Snake([5,5], 5, Defines.right)
boarder = Boarder.Boarder([20, 20])

def clear_game():
    snake1.print_snake(" ")


def print_game():
    snake1.print_snake("X")
    boarder.print_boarder()
    time.sleep(1)


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