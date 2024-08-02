import pygame

DISPLAY_W, DISPLAY_H = 720, 480
screen = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))
clock = pygame.time.Clock()
game_state = "start"
start_time = 0
current_score = 0
final_score = 0

game_music = {
    'game_start'  : 'audio/start_bgm.wav',
    'game_running' : 'audio/main_bgm.wav',
    'game_over' : 'audio/game_over_bgm.wav'
}