import Data, Block, Rule, DrawFirst, InitPeople, Income


def run_view():
    evacuation_time = 0  # 疏散时间步 计时器
    allPeople = InitPeople.creatAppointPeo()  # 初始化行人--初始化指定行人 便于调试
    DrawFirst.drawPeople(allPeople)  # 绘制行人和地图
    while Data.flag:  # 循环标识符
        for p in allPeople:  # 遍历每个行人
            direcetion = Income.countDirectionIncome(p)  # 计算每个行人的移动方向
            Rule.PeopleMove(p, direcetion)  # 行人移动
            Rule.chickOverAround(p, allPeople)  # 检测是否到达出口
        DrawFirst.drawPeople(allPeople)  # 更新图像

        '''程序终止检测'''
        if len(allPeople) == 0:  # 如果行人都出去了
            Data.flag = False  # 更改循环标识符
        evacuation_time += 1  # 疏散时间步 计时器+1
        print('当前时间步:', evacuation_time)  # 输出信息


if __name__ == '__main__':
    '''程序入口方法'''
    run_view()
