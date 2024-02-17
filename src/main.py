import pygame as pg  # in pipfreeze
from pygame import display, event, time
from drawing import Drawing

from config import *
from player import Player
from pawn import Pawn


def main():
    pg.init()
    sc = display.set_mode((WIDTH, HEIGHT))
    clock = time.Clock()
    player = Player()
    pawns = Pawn(pawn_cnt)
    drawing = Drawing(sc)
    dt = 0
    while True:
        for ev in event.get():
            if ev.type == pg.QUIT:
                exit()
        car_x, car_y = player.pos()
        drawing.background(dt)
        drawing.player(car_x, car_y)
        for i in range(0, pawn_cnt):
            p_x, p_y = pawns.pos(i)
            drawing.npc(p_x, p_y, i, pawns.get_color(i))
            pawns.movement(i, dt)
            if ((car_x < (p_x + player_size[0] - 5) and
                 (car_x + player_size[0]) > p_x + 5) and
                    (car_y < (p_y + player_size[1]) - 5 and
                     (car_y + player_size[1]) > p_y + 5)):
                player = Player()
                pawns = Pawn(pawn_cnt)
                break
        drawing.fps(clock)
        player.movement(dt)
        display.flip()
        dt = clock.tick(FPS)


if __name__ == '__main__':
    main()
