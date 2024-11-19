import pygame
from constants import *
from player import Player


class Game_Over():
    
    def game_over(self):
        font = pygame.font.Font(None, 180)
        text = font.render("Game Over!", True, (255, 0, 0))
        text_rect = text.get_rect(center=(1280 / 2, 720 / 2 - 100))
        return text, text_rect
    
    def game_score(self, score, game_running):
        if game_running == False:
            font = pygame.font.Font(None, 100)
            text = font.render(f"Score: {score}", True, (255,255,255))
            text_rect = text.get_rect(center=(1280 / 2, 720 / 2 + 100))
            return text, text_rect
        else:
            font_2 = pygame.font.Font(None, 36)
            text_2 = font_2.render(f"Score: {score}", True, (255,255,255))
            text_rect_2 = text_2.get_rect(topright=(1260, 20))
            return text_2, text_rect_2        