import Defines
import curses

class Element:


    def __init__(self, pos = [0, 0], rgb = Defines.default_rgb):
        self.position = []
        self.rgb_val = []

        self.set_pos(pos)
        self.set_color(rgb)

    def set_color(self, rgb):
        for i in rgb:
            if i < 0 and i > 255:
                return
        self.rgb_val = rgb

    def get_color(self):
        return self.rgb_val

    def set_pos(self, pos):
        if pos[Defines.x] < Defines.geometry[Defines.x] or pos[Defines.y] < Defines.geometry[Defines.y]:
            self.position = pos

    def get_pos(self):
        return self.position
    
    def print_element(self, c):
        x = self.position[Defines.x]
        y = self.position[Defines.y]

        #print(self.position)
        print("\033["+str(y)+";"+str(x)+"H"+c)


