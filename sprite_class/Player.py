import pygame
from utils import get_player_idle_frames, get_player_moving_frames, get_player_jump_image, ground
from globals import screen

# player sprite class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.player_idle_frames = get_player_idle_frames()
        self.player_move_frames = get_player_moving_frames()
        self.player_idle_index = 0
        self.player_move_index = 0
        
        self.image = self.player_idle_frames[self.player_idle_index]
        self.rect = self.image.get_rect(bottomleft = ((150, screen.get_height() - 200 + 8)))
        
        self.prev_x_pos = self.rect.x
        self.prev_y_pos = self.rect.y

        self.gravity = 0
        self.x_velocity = 0
        self.player_state = 'idle'
        
        self.jump_music = pygame.mixer.Sound('audio/jump.wav')
        
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom == 390: 
            self.gravity = -17
            self.jump_music.play()
        
        if keys[pygame.K_a]: self.x_velocity = -3
        
        if keys[pygame.K_d]: self.x_velocity = 3
        
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 390:
            self.rect.bottom = 390  
            
    def player_animation(self):
        if self.rect.bottom <= 390:
            # idle or moving
            if self.player_state == 'idle':
                
                self.player_idle_index += 0.5
            
                if self.player_idle_index >= len(self.player_idle_frames): self.player_idle_index = 0
                self.image = self.player_idle_frames[int(self.player_idle_index)]
                
            elif self.player_state == 'moving':
                self.player_move_index += 0.5
                
                if self.player_move_index >= len(self.player_move_frames): self.player_move_index = 0
                self.image = self.player_move_frames[int(self.player_move_index)]
                
            elif self.player_state == 'jumping':
                self.image = get_player_jump_image()
                
    def render_player_state(self):
        # player is moving
        if self.prev_x_pos != self.rect.x : 
            self.player_state = 'moving'
            self.prev_x_pos = self.rect.x
        # player is idle
        elif self.prev_x_pos == self.rect.x: self.player_state = 'idle'  
        
        # player is jumping
        if self.rect.bottom < 390 : self.player_state = 'jumping' 
    
    def update(self):
        #player update all functions
        self.player_input()
        self.apply_gravity()
        self.player_animation()
        self.render_player_state()
        
        # player movement update
        self.rect.x += self.x_velocity
        self.x_velocity = 0
        
        # hitbox test
        # pygame.draw.rect(screen, 'pink', self.rect, 2)
        