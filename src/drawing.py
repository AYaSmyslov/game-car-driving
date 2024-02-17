import pygame as pg
from pygame import font, image, transform

from config import *
from map import txt_map, dict_road

class Drawing:
    def __init__(self, sc):
        self.sc = sc
        self.font = font.Font('fonts/main.ttf', 36)

        self.road = image.load('img/road.png').convert_alpha()
        self.road = transform.scale(self.road, (640, 320))

        self.car = image.load('img/car.png').convert_alpha()
        self.car = transform.scale(self.car, (400, 320))

        self.h_y = -160
    
    def background(self, dt):
        x, y = 0, 0
        for row in txt_map:
            for char in row:
                self.sc.blit(self.road, (x, y + self.h_y), dict_road[char])
                x = x + 160
            x = 0
            y = y + 160
        if self.h_y < 0:
            self.h_y += 0.4 * dt
        else:
            self.h_y -= 160.0

    def player(self, x, y):
        self.sc.blit(self.car, (x, y), (0, 0, 80, 160))

    def npc(self, x, y, i, color_id=0):
        if f_oncoming and ((WIDTH // 2) > x):
            self.sc.blit(self.car, (x, y), (80+80*color_id, 160, 80, 160))
        else:
            self.sc.blit(self.car, (x, y), (80+80*color_id, 0, 80, 160))

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, RED)
        self.sc.blit(render, FPS_POS)