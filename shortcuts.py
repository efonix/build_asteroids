import pygame
import sys
from player import *

pygame.init()

class shortcuts():

    def __init__(self):
        self.keys = None

    def update_keys(self):
        self.keys = pygame.key.get_pressed()

    def exit_game_shortcut(self):
        if (self.keys[pygame.K_LCTRL] or self.keys[pygame.K_RCTRL]) and self.keys[pygame.K_w]:
            pygame.quit()
            sys.exit()

    def restart_game_shortcut(self, player):
        if self.keys[pygame.K_r]:
            player.reset()
            return True
        return False
            