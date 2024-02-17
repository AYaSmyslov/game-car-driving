from config import *

txt_map = []
for i in range(0, cnt_map_rows):
    txt_map.append('')
    for j in range(0, cnt_roads):
        if f_oncoming: # Встречка вкл
            if cnt_roads == 2: # Два потока
                if j == 0:
                    txt_map[i] += '3'
                elif j == cnt_roads-1:
                    txt_map[i] += '4'
            else: # Больше двух потоков
                if j == 0:
                    txt_map[i] += '1'
                elif j == cnt_roads-1:
                    txt_map[i] += '2'
                elif j + 1 == cnt_roads // 2:
                    txt_map[i] += '7'
                elif j == cnt_roads // 2:
                    txt_map[i] += '8'
                else:
                    txt_map[i] += '6'
        else: # Встречка выкл
            if j == 0:
                txt_map[i] += '1'
            elif j == cnt_roads-1:
                txt_map[i] += '2'
            else:
                txt_map[i] += '6'
# print(txt_map)

dict_road = {
    '1': (0, 0, 160, 160),
    '2': (160, 0, 160, 160),
    '3': (320, 0, 160, 160),
    '4': (480, 0, 160, 160),
    '5': (0, 160, 160, 160),
    '6': (160, 160, 160, 160),
    '7': (320, 160, 160, 160),
    '8': (480, 160, 160, 160),
}