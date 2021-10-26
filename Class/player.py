from datetime import timedelta

import pygame

from Class.clock_game import its_night
from Fonction.visuel import coord_button


class Player:
    def __init__(self):
        self.username = ""
        self.energy = 100
        self.money = 0
        self.stock_code = 0
        self.stress = 0
        self.activity = "work"

        self.pass_dec_ener = 0.1
        self.acti_dec_ener = 0.5
        self.pass_sleep_ener = 0.3

        self.night_hour = 21
        self.night_min = 0
        self.morning_hour = 8
        self.morning_min = 0

    def get_energy(self):
        return self.energy

    def get_money(self):
        return self.money

    def get_stock_code(self):
        return self.stock_code

    def get_stress(self):
        return self.stress

    def inc_energy(self, energy):
        self.energy += energy

    def inc_money(self, money):
        self.money += money

    def inc_stock_code(self, stock_code):
        self.stock_code += stock_code

    def inc_stress(self, stress):
        self.stress += stress

    def passive_energy(self, hour, min):
        if self.activity == "work":
            malus = 2 if its_night(self.night_hour, self.night_min, self.morning_hour, self.morning_min, hour, min) else 1
            self.energy = self.energy - (self.pass_dec_ener * malus) if self.energy > 0 else 0
        elif self.activity == "sleep":
            bonus = 2 if its_night(self.night_hour, self.night_min, self.morning_hour, self.morning_min, hour, min) else 1
            self.energy = self.energy + (self.pass_sleep_ener * bonus) if self.energy < 100 else 100
        print(self.energy)

    def active_decrease_energy(self):
        self.energy -= self.acti_dec_ener

    def update_progress_energy(self, screen, w, h):
        back_bar_color = (60, 63, 60)
        back_bar_position = coord_button(5, 1, 20, 3, w, h)
        bar_color = "yellow"
        bar_position = coord_button(5, 1, self.energy*20/100, 3, w, h)
        pygame.draw.rect(screen, back_bar_color, back_bar_position)
        pygame.draw.rect(screen, bar_color, bar_position)
