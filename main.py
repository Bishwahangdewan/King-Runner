import pygame
import sys, time
from random import randint
from utils import get_player_idle_frames, get_player_moving_frames, get_enemy_moving_frames, get_player_jump_image
from globals import DISPLAY_H, DISPLAY_W, screen, clock, game_state, start_time, current_score, final_score
from sprite_class.Coin import Coin
from sprite_class.Player import Player
from sprite_class.Enemy import Enemy

pygame.init()

game_music = {
    'game_start'  : 'audio/start_bgm.wav',
    'game_running' : 'audio/main_bgm.wav',
    'game_over' : 'audio/game_over_bgm.wav'
}

coin_sound = pygame.mixer.Sound('audio/coin.wav')


# import background screen
background = pygame.image.load('sprites/background.png').convert()
background = pygame.transform.scale(background, screen.get_size())

#import ground asset
ground = pygame.image.load('sprites/ground.png').convert()
pygame.transform.scale(ground, (screen.get_width(), ground.get_height()))
ground.set_colorkey((255, 255, 255))
ground_rect = ground.get_rect(bottomleft = (0, screen.get_height()))

# import fonts and texts
game_font = pygame.font.Font('font/arcade.ttf', 30)
game_font_small = pygame.font.Font('font/arcade.ttf', 15)
text_surface = game_font.render('King Runner', False, 'Black')
text_surface_rect = text_surface.get_rect(center = (screen.get_width() / 2, 30))

game_over_text = game_font.render('Game Over', False, 'Black')
game_over_text_rect = game_over_text.get_rect(center = (screen.get_width() / 2, screen.get_height() / 2))

game_restart_text = game_font_small.render('Press SPACE to play again!', False, 'Black')
game_restart_text_rect = game_restart_text.get_rect(center = (screen.get_width() / 2, 310))

# Game start screen player moving animation
move_frames = get_player_moving_frames()
move_index = 0

# display score
def display_score():
    # current_score = pygame.time.get_ticks() - start_time
    # current_score_text = game_font_small.render(f'Score {int(current_score/ 1000)}', False, 'Black')
    # current_score_rect = current_score_text.get_rect(center = (screen.get_width() / 2, 60))
    
    current_score_text = game_font_small.render(f'Score {int(current_score)}', False, 'Black')
    current_score_rect = current_score_text.get_rect(center = (screen.get_width() / 2, 60))
    screen.blit(current_score_text, current_score_rect)
    return current_score


#enemies spawn
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

#coin spawn
coin_timer = pygame.USEREVENT + 1
pygame.time.set_timer(coin_timer, 1500)

            
# Player sprite class group
playerSprite = pygame.sprite.GroupSingle()
playerSprite.add(Player ())

#Enemy sprite class group
enemySprite = pygame.sprite.Group()

#CoinSprite class group
coinSprite = pygame.sprite.Group()

def collision_sprite():
    global game_state, final_score, current_score
    
    if pygame.sprite.spritecollide(playerSprite.sprite, enemySprite, False):
        # game over
        enemySprite.empty()
        game_state = 'over'
        play_music()
        final_score = display_score()
        return False
    
    elif pygame.sprite.spritecollide(playerSprite.sprite, coinSprite, False):
        collided_coins = pygame.sprite.spritecollide(playerSprite.sprite, coinSprite, False)
        for coin in collided_coins:
            coin.kill()
            current_score += 20
       
        coin_sound.play()
        return True
    else:
        return True
    
    
def play_music():
    
    pygame.mixer.music.stop()
    
    if game_state == 'start':
        pygame.mixer.music.load(game_music['game_start'])
        pygame.mixer.music.play(-1)
        
    if game_state == 'running':
        pygame.mixer.music.load(game_music['game_running'])
        pygame.mixer.music.play(-1)
        
    if game_state == 'over':
        pygame.mixer.music.load(game_music['game_over'])
        pygame.mixer.music.play(-1)

# initial music play at first    
play_music()
    

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
                
        if game_state == 'over':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_state = 'running'
                    current_score = 0
                    play_music()
                    
        elif game_state == 'start':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_state = 'running'
                    play_music()
                    
        if event.type == obstacle_timer and game_state == 'running':
            enemySprite.add(Enemy())
            
        if event.type == coin_timer and game_state == 'running':
            coinSprite.add(Coin())
            
  
                
    # main game         
    if game_state == 'running':
        # blit
        screen.fill('cyan')
        screen.blit(background, (0,0))
        screen.blit(ground, ground_rect)
        screen.blit(text_surface, text_surface_rect)
              
        # display score
        score = display_score()
        
        # player sprite draw
        playerSprite.draw(screen)
        playerSprite.update()
        
        #enemy sprite draw
        enemySprite.draw(screen)
        enemySprite.update()
        
        #coin sprite draw
        coinSprite.draw(screen)
        coinSprite.update()
        
        collision_sprite()
            
            
    if game_state == 'over':
        # game over screen
         screen.blit(background, (0,0))
         screen.blit(game_over_text, game_over_text_rect)
         screen.blit(game_restart_text, game_restart_text_rect)
         
         final_score_text = game_font_small.render(f'Your score {int(final_score)}', False, 'Black')
         final_score_rect = final_score_text.get_rect(center=(screen.get_width() / 2, 280))
         screen.blit(final_score_text, final_score_rect)
         
         player_x_velocity = 0
         start_time = pygame.time.get_ticks()
         
         
    if game_state == 'start':
        # start screen
        screen.blit(background, (0,0))
        start_text_main = game_font.render('King Runner', False, 'Black')
        start_text_rect = start_text_main.get_rect(center = (screen.get_width() / 2, 150))
        
        start_instruction_text = game_font_small.render('Press SPACE  to play!', False, 'Black')
        start_instruction_text_rect = start_instruction_text.get_rect(center = (screen.get_width() /2, 320))
        
        
        # king moving animation
        move_index += 0.3
        if move_index >= len(move_frames) : move_index =0
        
        start_player_image = move_frames[int(move_index)]
        
        # scale the image
        start_player_image = pygame.transform.scale(start_player_image, (start_player_image.get_width() * 2, start_player_image.get_height() * 2))
        start_player_image_rect = start_player_image.get_rect(center = ((screen.get_width() / 2) - 10, 240))
        
        # play start music
        
        
        screen.blit(start_text_main,start_text_rect)
        screen.blit(start_player_image, start_player_image_rect)
        screen.blit(start_instruction_text, start_instruction_text_rect)
    
   
    # update every frame
    pygame.display.update()

    # maintain 60 fps
    clock.tick(60)

