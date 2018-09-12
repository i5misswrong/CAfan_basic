import math
import numpy as np


def countDirectionIncome(p):
    '''
    计算行人的收益
    :param p: 单个行人
    :return: 方向 int
    '''
    around = getPedestrianAround(p)  # 计算行人周围坐标  返回一个列表 可以debug查看一下
    direction_income = []  # 行人收益存放列表
    for i in around:  # 遍历around 需要循环2次  根据around结构具体调节循环次数
        for j in i:
            try:  # 在程序终止时 除数为0  捕获异常 完成程序
                dir_income = 1 / math.sqrt((j[0] - 20) ** 2 + (j[1] - 40) ** 2)  # 计算行人周围8个位置到出口的距离 的倒数
            except:
                print('除数为0')
            direction_income.append(dir_income)  # 将计算的收益添加到列表
    return np.argmax(direction_income)  # 获取最大收益的 列表的下角标 即行人的运动方向


def getPedestrianAround(p):
    '''
    获取行人周围8个点的坐标
    :param p: 单个行人
    :return: 返回值可以debug看一下结构
    '''
    around = []
    around.append(([p.x - 1, p.y + 1], [p.x, p.y + 1], [p.x + 1, p.y + 1], [p.x - 1, p.y], [p.x, p.y], [p.x + 1, p.y],
                   [p.x - 1, p.y - 1], [p.x, p.y - 1], [p.x + 1, p.y - 1]))
    return around
