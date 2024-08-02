import pygame
from globals import screen

def get_player_idle_frames():
    player_idle_img_1 = pygame.image.load('sprites/king/king_1.png').convert_alpha()
    player_idle_img_1 = pygame.transform.scale(player_idle_img_1, (player_idle_img_1.get_width() * 1.5, player_idle_img_1.get_height() * 1.5))

    player_idle_img_2 = pygame.image.load('sprites/king/king_2.png').convert_alpha()
    player_idle_img_2 = pygame.transform.scale(player_idle_img_2, (player_idle_img_2.get_width() * 1.5, player_idle_img_2.get_height() * 1.5))

    player_idle_img_3 = pygame.image.load('sprites/king/king_3.png').convert_alpha()
    player_idle_img_3 = pygame.transform.scale(player_idle_img_3, (player_idle_img_3.get_width() * 1.5, player_idle_img_3.get_height() * 1.5))

    player_idle_img_4 = pygame.image.load('sprites/king/king_4.png').convert_alpha()
    player_idle_img_4 = pygame.transform.scale(player_idle_img_4, (player_idle_img_4.get_width() * 1.5, player_idle_img_4.get_height() * 1.5))

    player_idle_img_5 = pygame.image.load('sprites/king/king_5.png').convert_alpha()
    player_idle_img_5 = pygame.transform.scale(player_idle_img_5, (player_idle_img_5.get_width() * 1.5, player_idle_img_5.get_height() * 1.5))

    player_idle_img_6 = pygame.image.load('sprites/king/king_6.png').convert_alpha()
    player_idle_img_6 = pygame.transform.scale(player_idle_img_6, (player_idle_img_6.get_width() * 1.5, player_idle_img_6.get_height() * 1.5))

    player_idle_img_7 = pygame.image.load('sprites/king/king_7.png').convert_alpha()
    player_idle_img_7 = pygame.transform.scale(player_idle_img_7, (player_idle_img_7.get_width() * 1.5, player_idle_img_7.get_height() * 1.5))
        
    player_idle_img_8 = pygame.image.load('sprites/king/king_8.png').convert_alpha()
    player_idle_img_8 = pygame.transform.scale(player_idle_img_8, (player_idle_img_8.get_width() * 1.5, player_idle_img_8.get_height() * 1.5))

    player_idle_img_9 = pygame.image.load('sprites/king/king_9.png').convert_alpha()
    player_idle_img_9 = pygame.transform.scale(player_idle_img_9, (player_idle_img_9.get_width() * 1.5, player_idle_img_9.get_height() * 1.5))

    player_idle_img_10 = pygame.image.load('sprites/king/king_10.png').convert_alpha()
    player_idle_img_10 = pygame.transform.scale(player_idle_img_10, (player_idle_img_10.get_width() * 1.5, player_idle_img_10.get_height() * 1.5))

    player_idle_img_11 = pygame.image.load('sprites/king/king_11.png').convert_alpha()
    player_idle_img_11 = pygame.transform.scale(player_idle_img_11, (player_idle_img_11.get_width() * 1.5, player_idle_img_11.get_height() * 1.5))

    player_idle_frames = [
        player_idle_img_1,
        player_idle_img_2,
        player_idle_img_3,
        player_idle_img_4,
        player_idle_img_5,
        player_idle_img_6,
        player_idle_img_7,
        player_idle_img_8,
        player_idle_img_9,
        player_idle_img_10,
        player_idle_img_11,
    ]
    
    return player_idle_frames

    
def get_player_moving_frames():
    player_move_img_1 = pygame.image.load('sprites/king_move/king_move_1.png').convert_alpha()
    player_move_img_1 = pygame.transform.scale(player_move_img_1, (player_move_img_1.get_width() * 1.5, player_move_img_1.get_height() * 1.5))

    player_move_img_2 = pygame.image.load('sprites/king_move/king_move_2.png').convert_alpha()
    player_move_img_2 = pygame.transform.scale(player_move_img_2, (player_move_img_2.get_width() * 1.5, player_move_img_2.get_height() * 1.5))

    player_move_img_3 = pygame.image.load('sprites/king_move/king_move_3.png').convert_alpha()
    player_move_img_3 = pygame.transform.scale(player_move_img_3, (player_move_img_3.get_width() * 1.5, player_move_img_3.get_height() * 1.5))

    player_move_img_4 = pygame.image.load('sprites/king_move/king_move_4.png').convert_alpha()
    player_move_img_4 = pygame.transform.scale(player_move_img_4, (player_move_img_4.get_width() * 1.5, player_move_img_4.get_height() * 1.5))

    player_move_img_5 = pygame.image.load('sprites/king_move/king_move_5.png').convert_alpha()
    player_move_img_5 = pygame.transform.scale(player_move_img_5, (player_move_img_5.get_width() * 1.5, player_move_img_5.get_height() * 1.5))

    player_move_img_6 = pygame.image.load('sprites/king_move/king_move_6.png').convert_alpha()
    player_move_img_6 = pygame.transform.scale(player_move_img_6, (player_move_img_6.get_width() * 1.5, player_move_img_6.get_height() * 1.5))

    player_move_img_7 = pygame.image.load('sprites/king_move/king_move_7.png').convert_alpha()
    player_move_img_7 = pygame.transform.scale(player_move_img_7, (player_move_img_7.get_width() * 1.5, player_move_img_7.get_height() * 1.5))

    player_move_img_8 = pygame.image.load('sprites/king_move/king_move_8.png').convert_alpha()
    player_move_img_8 = pygame.transform.scale(player_move_img_8, (player_move_img_8.get_width() * 1.5, player_move_img_8.get_height() * 1.5))

    player_move_frames = [
        player_move_img_1,
        player_move_img_2,
        player_move_img_3,
        player_move_img_4,
        player_move_img_5,
        player_move_img_6,
        player_move_img_7,
        player_move_img_8,
    ]

    
    return player_move_frames


def get_enemy_moving_frames():
    enemy_move_img_1 = pygame.image.load('sprites/pig/pig_1.png').convert_alpha()
    enemy_move_img_1 = pygame.transform.scale(enemy_move_img_1, (enemy_move_img_1.get_width() * 2, enemy_move_img_1.get_height() * 2))
    
    enemy_move_img_2 = pygame.image.load('sprites/pig/pig_2.png').convert_alpha()
    enemy_move_img_2 = pygame.transform.scale(enemy_move_img_2, (enemy_move_img_2.get_width() * 2, enemy_move_img_2.get_height() * 2))
    
    enemy_move_img_3 = pygame.image.load('sprites/pig/pig_3.png').convert_alpha()
    enemy_move_img_3 = pygame.transform.scale(enemy_move_img_3, (enemy_move_img_3.get_width() * 2, enemy_move_img_3.get_height() * 2))
    
    enemy_move_img_4 = pygame.image.load('sprites/pig/pig_4.png').convert_alpha()
    enemy_move_img_4 = pygame.transform.scale(enemy_move_img_4, (enemy_move_img_4.get_width() * 2, enemy_move_img_4.get_height() * 2))
    
    enemy_move_img_5 = pygame.image.load('sprites/pig/pig_5.png').convert_alpha()
    enemy_move_img_5 = pygame.transform.scale(enemy_move_img_5, (enemy_move_img_5.get_width() * 2, enemy_move_img_5.get_height() * 2))
    
    enemy_move_img_6 = pygame.image.load('sprites/pig/pig_6.png').convert_alpha()
    enemy_move_img_6 = pygame.transform.scale(enemy_move_img_6, (enemy_move_img_6.get_width() * 2, enemy_move_img_6.get_height() * 2))
    
    enemy_move_frames = [
        enemy_move_img_1,
        enemy_move_img_2,
        enemy_move_img_3,
        enemy_move_img_4,
        enemy_move_img_5,
        enemy_move_img_6
    ]
    
    return enemy_move_frames


def get_player_jump_image():
    player_jump_image = pygame.image.load('sprites/king/king_jump.png').convert_alpha()
    player_jump_image = pygame.transform.scale(player_jump_image, (player_jump_image.get_width() * 1.5, player_jump_image.get_height() * 1.5))
    
    return player_jump_image


def get_coin_frames():
    coin_image_1 = pygame.image.load('sprites/coin/coin_1.png').convert_alpha()
    coin_image_1 = pygame.transform.scale(coin_image_1, (coin_image_1.get_width() * 2, coin_image_1.get_height() * 2))
    
    coin_image_2 = pygame.image.load('sprites/coin/coin_2.png').convert_alpha()
    coin_image_2 = pygame.transform.scale(coin_image_2, (coin_image_2.get_width() * 2, coin_image_2.get_height() * 2))
    
    coin_image_3 = pygame.image.load('sprites/coin/coin_3.png').convert_alpha()
    coin_image_3 = pygame.transform.scale(coin_image_3, (coin_image_3.get_width() * 2, coin_image_3.get_height() * 2))
    
    coin_image_4 = pygame.image.load('sprites/coin/coin_4.png').convert_alpha()
    coin_image_4 = pygame.transform.scale(coin_image_4, (coin_image_4.get_width() * 2, coin_image_4.get_height() * 2))
    
    coin_image_5 = pygame.image.load('sprites/coin/coin_5.png').convert_alpha()
    coin_image_5 = pygame.transform.scale(coin_image_5, (coin_image_5.get_width() * 2, coin_image_5.get_height() * 2))
    
    coin_image_6 = pygame.image.load('sprites/coin/coin_6.png').convert_alpha()
    coin_image_6 = pygame.transform.scale(coin_image_6, (coin_image_6.get_width() * 2, coin_image_6.get_height() * 2))
    
    coin_image_7 = pygame.image.load('sprites/coin/coin_7.png').convert_alpha()
    coin_image_7 = pygame.transform.scale(coin_image_7, (coin_image_7.get_width() * 2, coin_image_7.get_height() * 2))
    
    coin_image_8 = pygame.image.load('sprites/coin/coin_8.png').convert_alpha()
    coin_image_8 = pygame.transform.scale(coin_image_8, (coin_image_8.get_width() * 2, coin_image_8.get_height() * 2))
    
    coin_image_9 = pygame.image.load('sprites/coin/coin_9.png').convert_alpha()
    coin_image_9 = pygame.transform.scale(coin_image_9, (coin_image_9.get_width() * 2, coin_image_9.get_height() * 2))
    
    coin_image_10 = pygame.image.load('sprites/coin/coin_10.png').convert_alpha()
    coin_image_10 = pygame.transform.scale(coin_image_10, (coin_image_10.get_width() * 2, coin_image_10.get_height() * 2))
    
    coin_image_11 = pygame.image.load('sprites/coin/coin_11.png').convert_alpha()
    coin_image_11 = pygame.transform.scale(coin_image_11, (coin_image_11.get_width() * 2, coin_image_11.get_height() * 2))
    
    coin_image_12 = pygame.image.load('sprites/coin/coin_12.png').convert_alpha()
    coin_image_12 = pygame.transform.scale(coin_image_12, (coin_image_12.get_width() * 1.5, coin_image_12.get_height() * 1.5))
    
    coin_frames = [
        coin_image_1,
        coin_image_2,
        coin_image_3,
        coin_image_4,
        coin_image_5,
        coin_image_6,
        coin_image_7,
        coin_image_8,
        coin_image_9,
        coin_image_10,
        coin_image_11,
        coin_image_12,
    ]
    
    return coin_frames


def get_player_dead_frames():
    king_dead_2 = pygame.image.load('sprites/king_dead/king_dead_2.png').convert_alpha()
    king_dead_2 = pygame.transform.scale(king_dead_2, (king_dead_2.get_width() * 1.5, king_dead_2.get_height() * 1.5))
    
    king_dead_3 = pygame.image.load('sprites/king_dead/king_dead_3.png').convert_alpha()
    king_dead_3 = pygame.transform.scale(king_dead_3, (king_dead_3.get_width() * 1.5, king_dead_3.get_height() * 1.5))
    
    king_dead_4 = pygame.image.load('sprites/king_dead/king_dead_4.png').convert_alpha()
    king_dead_4 = pygame.transform.scale(king_dead_4, (king_dead_4.get_width() * 1.5, king_dead_4.get_height() * 1.5))
    
    king_dead_frames = [
        king_dead_2,
        king_dead_3,
        king_dead_4
    ]
    
    return king_dead_frames



ground = pygame.image.load('sprites/ground.png').convert()
pygame.transform.scale(ground, (screen.get_width(), ground.get_height()))
ground.set_colorkey((255, 255, 255))
ground_rect = ground.get_rect(bottomleft = (0, screen.get_height()))
