import pygame
from pygame.locals import *

from Fonction.visuel import display_base, rect_with_alpha, display_image


class Menu:
    def __init__(self):
        self.clock_tick = 50
        self.running_game = True
        self.click = False
        self. first_time = True

    def run(self, clock, opt):
        while self.running_game:
            if opt.get_fullscreen() and not self.first_time:
                display_image(opt.get_w() , opt.get_h(), "Asset/HUD/bg/menu.PNG", screen)
                screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            else:
                screen = display_base(opt.get_w() , opt.get_h(), "Asset/HUD/bg/menu.PNG")
                self.first_time = False

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