import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shoot import Shot
from game_over import Game_Over
import sys

def main():
    pygame.init()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    game_over = Game_Over() 
    text, text_rect = game_over.game_over()

    game_running = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill(color=(0,0,0))
        if game_running == True:
            for update in updatable:
                update.update(dt)
            for draw in drawable:
                draw.draw(screen)
            for asteroid in asteroids:
                if player.collisions(asteroid):
                    game_running = False
                    break
                for shot in shots:
                    if shot.collisions(asteroid):
                        shot.kill()
                        asteroid.split()
            for asteroid in asteroids:
                if game_running == False:
                    asteroid.kill()
        else:
            screen.blit(text, text_rect)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                game_running = True
                player.reset()
        pygame.display.flip()
        dt = clock.tick(60) / 1000 #limit framrate to 60 FPS

if __name__ == "__main__":
    main()
