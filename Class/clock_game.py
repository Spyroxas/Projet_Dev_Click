import math
from datetime import timedelta, datetime
import datetime

import pygame.draw

from Fonction.visuel import DrawText


def refacto_format(hour, minute):
    if len(str(minute)) == 1:
        minute = "0" + str(minute)
    if len(str(hour)) == 1:
        hour = "0" + str(hour)
    return str(hour), str(minute)


def convert_degrees_to_pygame(r, theta):
    y = math.cos(2 * math.pi * theta/360) * r
    x = math.sin(2 * math.pi * theta/360) * r
    return x+4, -(y-4)


def clock_hand(center, radius, angle, thickness, color, screen):
    x = center[0] + radius * math.cos(math.radians(angle - 90))
    y = center[1] + radius * math.sin(math.radians(angle - 90))
    pygame.draw.line(screen, color, center, (int(x), int(y)), thickness)


def draw_markings(screen, x, y):
    d = 40
    d2 = 5
    pygame.draw.circle(screen, "white", (x, y), 50, 3)
    for i in range(0, 360, 15):
        x1 = x * 2 // 2 + d * math.cos(math.radians(i))
        y1 = y * 2 // 2 + d * math.sin(math.radians(i))
        x2 = x1 + d2 * math.cos(math.radians(i))
        y2 = y1 + d2 * math.sin(math.radians(i))
        pygame.draw.line(screen, "white", (x1, y1), (x2, y2), 2)


def its_night(night_hour, night_min, morning_hour, morning_min, hour, min):
    night = timedelta(hours=night_hour, minutes=night_min)
    actual_time = timedelta(hours=hour, minutes=min)
    morning = timedelta(hours=morning_hour, minutes=morning_min)
    return True if (night < actual_time or actual_time < morning) else False


class ClockGame:
    def __init__(self):
        self.minute = 0
        self.hour = 0
        self.inc_speed = 0
        self.speed = 10
        self.init_hour_minute(9, 0)
        self.date_game = 0
        self.date_since_start = 0

    def update_speed(self, speed):
        self.speed = speed

    def init_hour_minute(self, hour, minute):
        self.minute = minute
        self.hour = hour

    def init_date(self):
        curr_date = datetime.datetime.now().strftime("%m/%d/%y")
        self.date_game = datetime.datetime.strptime(curr_date, "%m/%d/%y").strftime("%A %d %B %Y")
        self.date_since_start = datetime.datetime.strptime("01/01/0001", "%m/%d/%Y").strftime("%A %d %B %Y")

    def show_main_clock(self, screen, p, x, y, size):
        self.inc_speed += 1
        if self.inc_speed >= self.speed:
            self.inc_speed = 0
            self.minute += 1
            p.passive_energy(self.hour, self.minute)
        if self.minute >= 60:
            self.minute = 0
            self.hour += 1
            if self.hour >= 24:
                self.hour = 0
                self.date_game = (datetime.datetime.strptime(str(self.date_game), "%A %d %B %Y") + datetime.timedelta(days=1)).strftime("%A %d %B %Y")
                self.date_since_start = (datetime.datetime.strptime(str(self.date_since_start), "%A %d %B %Y") + datetime.timedelta(days=1)).strftime("%A %d %B %Y")
        str_hour, str_minute = refacto_format(self.hour, self.minute)

        draw_markings(screen, x, y)
        clock_hand((x, y), 30, self.minute * 6, 3, "white", screen)
        clock_hand((x, y), 20, self.hour * 15, 3, "red", screen)

        DrawText(screen, str_hour + ":" + str_minute, "white", x, y, size)
        DrawText(screen, str(self.date_game), "white", 780, 80, 12)
        DrawText(screen, str(self.date_since_start), "white", 780, 90, 12)
