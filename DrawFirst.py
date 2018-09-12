import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
import numpy as np
import Data
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import time

'''绘制行人  主绘图方法'''


def drawPeople(P):
    plt.clf()  # 清除数据
    P_x = []  # 存放所有行人x坐标
    P_y = []  # 存放所有行人y坐标
    for p in P:  # 遍历行人
        P_x.append(p.x)  # 分别添加坐标
        P_y.append(p.y)
    plt.scatter(P_x, P_y, c='r', marker='s')  # 绘制行人

    drawWallAndExit()  # 绘制墙壁和出口

    '''由于无法右上角关闭 加了个关闭按钮'''
    closeFig = plt.axes([0.8, 0.025, 0.1, 0.04])  # 关闭按钮
    closeFigbutton = Button(closeFig, 'close', hovercolor='0.5')  # 按钮样式
    closeFigbutton.on_clicked(closeFigure)  # 按钮按下去的动作

    # plt.savefig("%d.png" %step) #保存图片用
    while Data.pause_flag:
        plt.pause(1)  # 暂停1s
    plt.pause(0.3)  # 暂停1s


'''关闭按钮动作'''


def closeFigure(event):
    plt.close()  # 将窗口关闭
    Data.flag = False  # 循环标记为Fasle


'''绘制墙壁和出口'''


def drawWallAndExit():
    '''墙壁为实线'''
    plt.plot([0, Data.ROOM_M], [0, 0], 'b-')  # down
    plt.plot([0, Data.EXIT_X_LEFT], [Data.ROOM_M, Data.ROOM_M], 'b-')  # up_LEFT
    plt.plot([Data.EXIT_X_RIGHT, Data.ROOM_M], [Data.ROOM_M, Data.ROOM_M], 'b-')  # up_LEFT
    plt.plot([0, 0], [0, Data.ROOM_N], 'b-')  # left and right
    plt.plot([Data.ROOM_M, Data.ROOM_M], [0, Data.ROOM_N], 'b-')

    '''绘制出口'''
    plt.plot([Data.EXIT_X_LEFT, Data.EXIT_X_RIGHT], [Data.ROOM_M, Data.ROOM_M], 'y--')
