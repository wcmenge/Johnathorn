from vector import Vector
import pygame
class PowerUp():

  
    def __init__(self, img, start_x, start_y, p_type,):
        self.img = img
        self.pos = Vector(0.0, 0.0)
        self.pos.x = start_x
        self.pos.y = start_y
        self.type = p_type
        bounding_box = (self.pos.x, self.pos.y, self.img.get_width(), self.img.get_height())
        self.bbox = bounding_box
        
    def draw(self, window):
        window.blit (self.img, (round(self.pos.x), round(self.pos.y)))
        
        

    def collide (self, other):
        """
        Uses pygame's built in collision detection to check whether
        two sprites collide based on their bounding boxes.
        """
        c_bool = self.get_bbox().colliderect(other.get_bbox())
        if c_bool:
            print("Colision")
            other.add_buff(self.type)
            return False
        else:
            return True
            
    def get_bbox (self):
        """
        Calculates the screen coordinate of the bounding box.
        """
        return pygame.Rect(self.pos.x, self.pos.y, self.bbox[2], self.bbox[3])
