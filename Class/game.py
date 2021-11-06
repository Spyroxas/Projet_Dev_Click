import pygame
from pygame.locals import *

from Class.clock_game import ClockGame
from Class.player import Player
from Fonction.visuel import coord_button, display_base, display_info_code, display_info_money, display_info_stock_code, \
    coord, rect_with_alpha


def bot_autominer(code, bot, tick):
    code += (bot/tick)
    return code


class Game:
    def __init__(self):
        self.running_game = True
        self.click = False
        self.dis_w = 1280
        self.dis_h = 720
        self.code = 0
        self.inc_code = 10
        self.inc_money = 1
        self.bot = 0
        self.inc_bot = 1
        self.cost = 2
        self.speed_time = 1
        self.clock_tick = 50
        self.clock_tick_bot = 0.6
        self.clock_bot = self.clock_tick * self.clock_tick_bot
        self.screen = display_base(self.dis_w, self.dis_h, "Asset/HUD/bg.PNG")
        self.pause = False

        self.cg = ClockGame()
        self.p = Player()
        self.cg.init_date()

    def update_progress_code(self):
        back_bar_color = (60, 63, 60)
        back_bar_position = coord_button(5, 5, 20, 3, self.dis_w, self.dis_h)
        bar_color = (111, 210, 46)
        bar_position = coord_button(5, 5, self.code*20/100, 3, self.dis_w, self.dis_h)
        pygame.draw.rect(self.screen, back_bar_color, back_bar_position)
        pygame.draw.rect(self.screen, bar_color, bar_position)

    def finish_a_code(self):
        if self.code >= 100:
            self.p.inc_stock_code(1)
            self.code = 0

    def update_speed_time(self, speed_time):
        if speed_time == 1:
            self.cg.update_speed(10)
            self.clock_bot = self.clock_tick * self.clock_tick_bot
        elif speed_time == 2:
            self.cg.update_speed(5)
            self.clock_bot = self.clock_tick * (self.clock_tick_bot * 2)
        else:
            self.cg.update_speed(2)
            self.clock_bot = self.clock_tick * (self.clock_tick_bot * 5)

    def run(self, clock):
        while self.running_game:

            pos = pygame.mouse.get_pos()

            if not self.pause:
                display_base(self.dis_w, self.dis_h, "Asset/HUD/bg.PNG")
                self.update_progress_code()
                self.p.update_progress_energy(self.screen, self.dis_w, self.dis_h)
                display_info_code(self.screen, self.code)
                display_info_stock_code(self.screen, self.p.stock_code)
                display_info_money(self.screen, self.p.get_money())

                pause = rect_with_alpha(self.screen, coord_button(70, 3, 6, 10, self.dis_w, self.dis_h),"Asset/HUD/button/menu/bouton-pause.png", 6, 10, self.dis_w, self.dis_h)
                if pause.collidepoint(pos) and self.click:
                    self.pause = True

                if self.p.activity == "work":
                    clicker = pygame.draw.rect(self.screen, "blue", coord_button(14.5, 14.5 , 68.5, 65, self.dis_w, self.dis_h))
                    clicker_image = pygame.image.load("Asset/HUD/clickers/clickers_1/c_1.PNG")
                    clicker_image = pygame.transform.scale(clicker_image, (coord(68.5, self.dis_w), coord(65, self.dis_h)))
                    self.screen.blit(clicker_image, clicker)
                    if clicker.collidepoint(pos) and self.p.energy > 0:
                        if self.click:
                            self.p.active_decrease_energy()
                            self.code += self.inc_code

                icon_activity = rect_with_alpha(self.screen, coord_button(95, 0, 10, 7, self.dis_w, self.dis_h), "Asset/HUD/button/activity/" + self.p.activity + ".png", 5, 7, self.dis_w, self.dis_h)
                if icon_activity.collidepoint(pos):
                    if self.click:
                        self.p.activity = "sleep" if self.p.activity == "work" else "work"

                icon_speed_time = rect_with_alpha(self.screen, coord_button(55, 3, 5, 3, self.dis_w, self.dis_h), "Asset/HUD/button/speed_clock/fleche_" + str(self.speed_time) + ".png", 3, 5, self.dis_w, self.dis_h)
                if icon_speed_time.collidepoint(pos):
                    if self.click:
                        self.speed_time = self.speed_time + 1 if self.speed_time < 3 else 1
                        self.update_speed_time(self.speed_time)

                if self.p.get_money() >= self.cost:
                    autocompletion = pygame.draw.rect(self.screen, "blue", coord_button(80, 90 , 20, 10, self.dis_w, self.dis_h))
                    if autocompletion.collidepoint(pos):
                        pygame.draw.rect(self.screen, "green", coord_button(80, 90 , 20, 10, self.dis_w, self.dis_h))
                        if self.click:
                            self.bot += self.inc_bot
                            self.code -= self.cost

                self.code = bot_autominer(self.code, self.bot, self.clock_bot)
                self.finish_a_code()

                # GESTION DES EVENTS
                self.click = False
                for event in pygame.event.get():
                    if event.type == QUIT:
                        self.running_game = False
                    elif event.type == MOUSEBUTTONDOWN:
                        self.click = True
                    elif event.type == KEYDOWN and event.key == K_ESCAPE:
                        self.pause = True

                self.cg.show_main_clock(self.screen, self.p, self.dis_w / 2, 50, 25)

            else:
                display_base(self.dis_w, self.dis_h, "Asset/HUD/bg-pause.PNG")
                pause = rect_with_alpha(self.screen, coord_button(80, 3, 6, 10, self.dis_w, self.dis_h), "Asset/HUD/button/menu/bouton-pause.png", 6, 10, self.dis_w, self.dis_h)
                if pause.collidepoint(pos) and self.click:
                    self.pause = False

                for event in pygame.event.get():
                    if event.type == QUIT:
                        self.running_game = False
                    elif event.type == MOUSEBUTTONDOWN:
                        self.click = True
                    elif event.type == KEYDOWN and event.key == K_ESCAPE:
                        self.pause = False
            pygame.display.update()
            clock.tick(self.clock_tick)
