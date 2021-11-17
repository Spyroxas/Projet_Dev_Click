import pygame

from Class.game import Game
from Class.option import Option
from Class.start_menu import StartMenu
from Class.menu import Menu

if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()
    option = Option()

    start = StartMenu()
    start.run(clock=clock, opt=option)

    menu = Menu()
    menu.run(clock=clock, opt=option)

    game = Game()
    game.run(clock=clock, opt=option)

pygame.quit()
quit()
