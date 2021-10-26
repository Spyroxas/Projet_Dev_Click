import pygame

from Class.game import Game

if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()

    # Menu
    game = Game()
    game.run(clock=clock)


pygame.quit()
quit()
