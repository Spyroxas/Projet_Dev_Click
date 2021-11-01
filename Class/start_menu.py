import pygame

from Fonction.visuel import display_base, coord_button, rect_with_alpha


class StartMenu:
    def __init__(self):
        self.dis_w = 1280
        self.dis_h = 720
        self.clock_tick = 50
        self.running_game = True
        self.click = False
        self.screen = display_base(self.dis_w, self.dis_h, "Asset/HUD/bg/start_menu.PNG")

    def run(self, clock):
        while self.running_game:
            pos = pygame.mouse.get_pos()

            start = rect_with_alpha(self.screen, coord_button(61, 28, 15, 6, self.dis_w, self.dis_h), "Asset/nothing.png", 5, 7, self.dis_w, self.dis_h)
            if start.collidepoint(pos):
                if self.click:
                    self.running_game = False

            # GESTION DES EVENTS
            self.click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.click = True

            pygame.display.update()
            clock.tick(self.clock_tick)