from random import randint, uniform
from config import *

class Pawn:
    def __init__(self, cnt):

        # Границы дороги
        self.x_begin, self.x_end = (0, 320)
        self.x_center_road = 40

        # Инициализация пешек
        self.x = [0] * cnt
        self.y = [0] * cnt
        self.color_id = [0] * cnt
        self.speed = [0.3] * cnt
        for i in range(0, cnt):
            self.respawn(i)

    def pos(self, pawn_id):
        """
        Возврат местоположения выбранной пешки
        Формальные параметры:
        self - экзмепляр класса;
        pawn_id - id пешки.
        """
        return self.x[pawn_id], self.y[pawn_id]

    def set_rand_pos(self, pawn_id, num_road=0):
        self.x[pawn_id] = self.x_center_road + (160 * num_road)
        self.x[pawn_id] += randint(-40, 40)
        return True

    def set_speed(self, pawn_id):
        if f_oncoming and (self.x[pawn_id] < (WIDTH // 2)):
            self.speed[pawn_id] = uniform(0.4, 0.6)
        else:
            self.speed[pawn_id] = uniform(0.3, 0.4)
        
    def set_rand_color(self, pawn_id):
        self.color_id[pawn_id] = randint(-1, 3)
    
    def get_color(self, pawn_id):
        return self.color_id[pawn_id]

    def need_respawn(self):
        for y_i in self.y:
            if y_i < HEIGHT:
                return False
        return True

    def two_road_spawn(self, pair_id=1):
        type_spawn = randint(pair_id-1, pair_id)
        road = randint(pair_id-1, pair_id)
        self.set_speed(pair_id)
        if type_spawn == 0: # One common line
            self.set_rand_pos(pair_id, road)
            self.set_rand_pos(pair_id-1, road)
            self.y[pair_id] = -160
            self.y[pair_id-1] = -360
            self.speed[pair_id-1] = self.speed[pair_id]
        else: # Two different lines
            self.set_rand_pos(pair_id, road)
            road += 1 if ((road % 2) == 0) else -1
            # ((road % 2) == 0): road += 1 else: road -= 1
            self.set_rand_pos(pair_id-1, road)
            self.y[pair_id] = -160
            self.y[pair_id-1] = -560
            self.set_speed(pair_id-1)
        self.set_rand_color(pair_id)
        self.set_rand_color(pair_id-1)

    def respawn(self, pawn_id):
        if cnt_roads == 2:
            self.two_road_spawn(pawn_id)
        elif cnt_roads > 2:
            for pair_id in range(1, cnt_roads, 2):
                self.two_road_spawn(pair_id)

        else:
            pass

    def movement(self, pawn_id, dt):
        if self.need_respawn():
            self.respawn(pawn_id)
        else:
            self.y[pawn_id] += self.speed[pawn_id] * dt