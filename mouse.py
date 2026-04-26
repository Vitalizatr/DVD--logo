from pyautogui import size
from pynput.mouse import Controller

mouse = Controller()
class MouseMovement:
    def __init__(self,_directions = [1,1]):
        self.directions = _directions

        self.screen_Width, self.screen_Height = size()
 
        self.mouse = Controller()

    def move_cursor(self):

        hits_wall = self.check_collision()
        if(hits_wall[0] or hits_wall[1]):
            self.change_direсtions(self.directions,*hits_wall)

        self.mouse.move(*self.directions)
        
    
    def check_collision(self):
        mouse_X, mouse_Y = self.mouse.position
        
        hit_X_wall = mouse_X >= self.screen_Width-2 or mouse_X <= 1
        hit_Y_wall = mouse_Y >= self.screen_Height-2 or mouse_Y <= 1

        return (hit_X_wall, hit_Y_wall)

    
    @staticmethod
    def change_direсtions(directions, direction_X = False, direction_Y = False):
        if direction_X:
            directions[0] *= -1
        if direction_Y:
            directions[1] *= -1
