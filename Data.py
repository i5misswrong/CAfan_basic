import numpy as np
import math

flag = True  # 程序循环标识符
pause_flag = False  # 程序暂停标记
ROOM_M = 40  # 房间长度
ROOM_N = 40  # 房间高度

EXIT_X_LEFT = 16  # 出口左边位置 x坐标
EXIT_X_RIGHT = 24  # 出口右边位置 x坐标

PEOPLE_DENSYTY = 0.1  # 行人密度
PEOPLE_NUMBER = int(ROOM_N * ROOM_M * PEOPLE_DENSYTY)  # 行人数量
