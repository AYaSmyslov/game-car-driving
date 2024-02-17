import pygame as pg
from config import *

class Player:
    def __init__(self):
        self.x, self.y = player_pos 
    
    def pos(self):
        return self.x, self.y

    def movement(self, dt):
        keys = pg.key.get_pressed()
        if keys[pg.K_w] or keys[pg.K_UP]:
            self.y += -0.2 * dt
        if keys[pg.K_s] or keys[pg.K_DOWN]:
            self.y += 0.6 * dt
        if keys[pg.K_a] or keys[pg.K_LEFT]:
            self.x += -0.4 * dt
        if keys[pg.K_d] or keys[pg.K_RIGHT]:
            self.x += 0.4 * dt