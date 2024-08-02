import pygame
from utils import get_enemy_moving_frames
from random import randint

#enemy sprite class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.enemy_move_frames = get_enemy_moving_frames()
        self.enemy_move_index = 0
        
        self.image = self.enemy_move_frames[self.enemy_move_index]
        self.rect = self.image.get_rect(bottomleft = (randint(700, 1000), 390))
        
        self.enemy_rect_list = []
        
    def enemy_animation(self):
        self.enemy_move_index += 0.2
        if self.enemy_move_index >= len(self.enemy_move_frames): self.enemy_move_index = 0
        self.image = self.enemy_move_frames[int(self.enemy_move_index)]
        
    def update(self):
        self.enemy_animation()
        # enemy movement
        self.rect.x -= 4
        
        # hitbox test
        # pygame.draw.rect(screen, 'pink', self.rect, 2)
        
        self.destroy()
        
    def destroy(self):
        if self.rect.x <= -100:
            self.kill()