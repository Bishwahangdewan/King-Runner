import pygame
from random import randint
from utils import get_coin_frames

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.coin_frames = get_coin_frames()
        self.coin_frame_index = 0
        
        self.image = self.coin_frames[self.coin_frame_index]
        self.rect = self.image.get_rect(bottomleft = (randint(700, 1200), 300))
        
        self.coin_state = 'moving'
        
        self.coin_rect_list = []
        
    def coin_animation(self):
        self.coin_frame_index += 0.2
        
        if self.coin_frame_index >= len(self.coin_frames) : self.coin_frame_index = 0
        self.image = self.coin_frames[int(self.coin_frame_index)]
        
    def update(self):
        self.coin_animation()
        
        # coin movement per frame
        if self.coin_state == 'moving':
            self.rect.x -= 4
        
        self.destroy()
            
    def destroy(self, coin_taken = False):
        if self.rect.x <= -100 or coin_taken == True:
            self.kill()
        