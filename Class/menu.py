import pygame
from pygame.locals import *

from Fonction.visuel import rect_with_alpha


class Menu:
    def __init__(self):
        self.clock_tick = 50
        self.running_game = True
        self.click = False
        self. first_time = True

    def run(self, clock, opt):
        while self.running_game:
            screen = opt.screen_management("Asset/HUD/bg/menu.PNG")

            pos = pygame.mouse.get_pos()

            start = rect_with_alpha(screen, 36, 65, 24, 10, "Asset/nothing.PNG", opt.get_w() , opt.get_h())
            if start.collidepoint(pos) and self.click:
                self.running_game = False

            option = rect_with_alpha(screen, 36, 80, 24, 10, "Asset/nothing.PNG", opt.get_w(), opt.get_h())
            if option.collidepoint(pos) and self.click:
                opt.set_running_game(True)
                opt.run(clock)

            # GESTION DES EVENTS
            self.click = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()
                elif event.type == MOUSEBUTTONDOWN:
                    self.click = True

            pygame.display.update()
            clock.tick(self.clock_tick)