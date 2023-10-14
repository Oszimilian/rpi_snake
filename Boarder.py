import Defines
from Element import Element

class Boarder:
    

    def __init__(self, pos = [10, 10]):
        self.boarder = []
        self.create_boarder(pos)

    def create_boarder(self, pos):
        for y in  range(0, pos[Defines.y]):
            for x in range(0, pos[Defines.x]):
                if y == 0 or y == pos[Defines.y] - 1:
                    self.boarder.append(Element([x, y], Defines.default_rgb))
                if x == 0 or x == pos[Defines.x] - 1:
                    self.boarder.append(Element([x, y], Defines.default_rgb))

    def check_collsion(self, pos, input_list):
        for i in self.boarder:
            if pos == input_list: 
                return False
            else:
                return True
            
    def print_boarder(self, sense):
        for i in self.boarder:
            i.print_element('X', sense)