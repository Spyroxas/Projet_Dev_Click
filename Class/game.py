import pygame
from pygame.locals import *

from Class.clock_game import ClockGame
from Class.player import Player
from Class.stock_exchange import StockExchange
from Fonction.visuel import coord_button, display_base, display_info_code, display_info_money, display_info_stock_code, \
    coord, rect_with_alpha, display_info_stock_exchange, display_base_alpha


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
        self.room = False

        self.cg = ClockGame()
        self.p = Player()

        self.se = StockExchange()
        self.cg.init_date()

    def update_progress_code(self, opt):
        back_bar_color = (60, 63, 60)
        back_bar_position = coord_button(5, 5, 20, 3, opt.get_w(), opt.get_h())
        bar_color = (111, 210, 46)
        bar_position = coord_button(5, 5, self.code*20/100, 3, opt.get_w(), opt.get_h())
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

    def run(self, clock, opt):
        while self.running_game:

            pos = pygame.mouse.get_pos()

            if not self.pause:
                self.screen = display_base(opt.get_w(), opt.get_h(), "Asset/HUD/bg/bg_room.png")
                if not self.room:
                    display_base_alpha(opt.get_w(), opt.get_h(), self.screen, "Asset/HUD/bg_opaque.PNG")
                    self.update_progress_code(opt)
                    self.p.update_progress_energy(self.screen, opt.get_w(), opt.get_h())
                    display_info_code(self.screen, self.code)
                    display_info_stock_code(self.screen, self.p.stock_code)
                    display_info_money(self.screen, self.p.get_money())

                bg_room = rect_with_alpha(self.screen, 10, 80, 6, 10, "Asset/HUD/button/background_button/bouton-bg.png", opt.get_w(), opt.get_h())
                if bg_room.collidepoint(pos) and self.click:
                    self.room = not self.room

                pause = rect_with_alpha(self.screen, 70, 3, 6, 10, "Asset/HUD/button/menu/bouton-pause.png", opt.get_w(), opt.get_h())
                if pause.collidepoint(pos) and self.click:
                    self.pause = True

                if not self.room:
                    if self.p.activity == "work":
                        clicker = rect_with_alpha(self.screen, 14.5, 14.5, 68.5, 65, "Asset/HUD/clickers/clickers_1/c_1.PNG", opt.get_w(), opt.get_h())
                        if clicker.collidepoint(pos) and self.p.energy > 0:
                            if self.click:
                                self.p.active_decrease_energy()
                                self.code += self.inc_code

                        w_stockexchange = rect_with_alpha(self.screen, 80, 40, 13, 10, "Asset/HUD/clickers/clickers_1/c_1.PNG", opt.get_w(), opt.get_h())
                        display_info_stock_exchange(self.screen, self.se.get_stock_exchange_prize())
                        if w_stockexchange.collidepoint(pos):
                            if self.click:
                                self.p.money += self.se.sale_code(self.p.stock_code)
                                self.p.stock_code = 0

                    icon_activity = rect_with_alpha(self.screen, 95, 0, 10, 7, "Asset/HUD/button/activity/" + self.p.activity + ".png", opt.get_w(), opt.get_h())
                    if icon_activity.collidepoint(pos):
                        if self.click:
                            self.p.activity = "sleep" if self.p.activity == "work" else "work"

                icon_speed_time = rect_with_alpha(self.screen, 55, 3, 5, 3, "Asset/HUD/button/speed_clock/fleche_" + str(self.speed_time) + ".png", opt.get_w(), opt.get_h())
                if icon_speed_time.collidepoint(pos):
                    if self.click:
                        self.speed_time = self.speed_time + 1 if self.speed_time < 3 else 1
                        self.update_speed_time(self.speed_time)

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

                self.cg.show_main_clock(self.screen, self.p, self.se, opt.get_w() / 2, 50, 25)

            else:
                display_base(opt.get_w(), opt.get_h(), "Asset/HUD/bg-pause.PNG")
                pause = rect_with_alpha(self.screen, 80, 3, 6, 10, "Asset/HUD/button/menu/bouton-pause.png", opt.get_w(), opt.get_h())
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
