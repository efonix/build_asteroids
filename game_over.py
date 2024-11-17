import pygame
from constants import *
from player import Player


class Game_Over():
    
    def game_over(self):
        font = pygame.font.Font(None, 180)
        text = font.render("Game Over!", True, (255, 0, 0))
        text_rect = text.get_rect(center=(1280 / 2, 720 / 2))
        return text, text_rect
        