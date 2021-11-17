import pygame
from pygame.locals import *

from Fonction.visuel import rect_with_alpha


class StartMenu:
    def __init__(self):
        self.dis_w = 1280
        self.dis_h = 720
        self.clock_tick = 50
        self.running_game = True
        self.click = False

    def run(self, clock, opt):
        while self.running_game:
            screen = opt.screen_management("Asset/HUD/bg/start_menu.PNG")

            pos = pygame.mouse.get_pos()

            start = rect_with_alpha(screen, 61, 28, 15, 6, "Asset/nothing.png", self.dis_w, self.dis_h)
            if start.collidepoint(pos):
                if self.click:
                    self.running_game = False

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