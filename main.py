import pygame

from Class.game import Game
from Class.start_menu import StartMenu
from Class.menu import Menu

if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()

    start = StartMenu()
    start.run(clock=clock)

    menu = Menu()
    menu.run(clock=clock)

    game = Game()
    game.run(clock=clock)


pygame.quit()
quit()
