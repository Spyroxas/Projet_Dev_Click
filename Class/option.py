import pygame
from pygame.locals import *

from Fonction.visuel import coord_button, rect_with_alpha, display_base


class Option:
    def __init__(self):
        self.dis_w = 1280
        self.dis_h = 720
        self.clock_tick = 50
        self.running_game = True
        self.click = False
        self.screen = display_base(self.dis_w, self.dis_h, "Asset/HUD/bg/option.png")

    def set_running_game(self, value):
        self.running_game = value

    def run(self, clock):
        while self.running_game:
            self.screen = display_base(self.dis_w, self.dis_h, "Asset/HUD/bg/option.png")

            pos = pygame.mouse.get_pos()

            start = rect_with_alpha(self.screen, coord_button(36, 65, 24, 10, self.dis_w, self.dis_h), "Asset/nothing.PNG", 5, 7, self.dis_w, self.dis_h)
            if start.collidepoint(pos) and self.click:
                self.running_game = False

            # GESTION DES EVENTS
            self.click = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()
                elif event.type == MOUSEBUTTONDOWN:
                    self.click = True
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    self.running_game = False

            pygame.display.update()
            clock.tick(self.clock_tick)
