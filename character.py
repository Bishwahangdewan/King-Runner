import pygame;

class Character:
    def __init__(self, filename, surface, x_pos, y_pos):
        #position of the image
        self.x_pos = x_pos
        self.y_pos = y_pos
        
        # load image
        self.image = pygame.image.load(filename).convert_alpha()
        self.image.set_colorkey((0, 0, 0))
        
        # get image height and width
        self.image_height = self.image.get_height()
        self.image_width = self.image.get_width()
        
        # surface the image to be rendered with
        self.surface = surface
        
    def update(self):
         self.surface.blit(
             pygame.transform.scale(self.image, (self.image_height * 2, self.image_width * 2)), 
             (self.x_pos, self.y_pos)
            )
        