import pygame
from pygame.locals import *

from Fonction.option_box import OptionBox
from Fonction.visuel import coord_button, display_base, display_image


class Option:
    def __init__(self):
        self.dis_w = 1280
        self.dis_h = 720
        self.clock_tick = 50
        self.running_game = True
        self.click = False
        self.screen = display_base(self.dis_w, self.dis_h, "Asset/HUD/bg/option.png")
        self.fullscreen = False

    def set_running_game(self, value):
        self.running_game = value

    def set_w_and_h(self, w, h):
        self.dis_w = w
        self.dis_h = h

    def get_w(self):
        return self.dis_w

    def get_h(self):
        return self.dis_h

    def get_w_and_h(self):
        return self.dis_w, self.dis_h

    def get_fullscreen(self):
        return self.fullscreen

    def get_screen(self):
        return self.screen

    def screen_management(self, image):
        if self.fullscreen:
            display_image(self.dis_w, self.dis_h, image, self.screen)
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        else:
            self.screen = display_base(self.dis_w, self.dis_h, image)
        return self.screen

    def run(self, clock):
        list1 = OptionBox(
            coord_button(20, 40, 20, 10, self.dis_w, self.dis_h)[0], coord_button(20, 40, 20, 10, self.dis_w, self.dis_h)[1],
            coord_button(20, 40, 20, 10, self.dis_w, self.dis_h)[2], coord_button(20, 40, 20, 10, self.dis_w, self.dis_h)[3],
            (150, 150, 150), (100, 200, 255), pygame.font.SysFont(None, 30), ["1280 x 720", "1920 x 1080", "plein écran"])

        while self.running_game:
            if self.fullscreen:
                display_image(self.dis_w, self.dis_h, "Asset/HUD/bg/option.png", self.screen)
                self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            else:
                self.screen = display_base(self.dis_w, self.dis_h, "Asset/HUD/bg/option.png")

            event_list = pygame.event.get()

            # GESTION DES EVENTS
            self.click = False
            for event in event_list:
                if event.type == QUIT:
                    pygame.quit()
                    quit()
                elif event.type == MOUSEBUTTONDOWN:
                    self.click = True
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    self.running_game = False

            selected_option = list1.update(event_list)
            if selected_option >= 0:
                if selected_option == 0:
                    self.set_w_and_h(1280, 720)
                    self.fullscreen = False
                if selected_option == 1:
                    self.set_w_and_h(1920, 1080)
                    self.fullscreen = False
                if selected_option == 2:
                    self.set_w_and_h(1920, 1080)
                    self.fullscreen = True

            list1.draw(self.screen)

            pygame.display.update()
            clock.tick(self.clock_tick)
