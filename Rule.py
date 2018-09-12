import Data


def PeopleMove(p, direction):
    '''
    行人移动方法
    :param p: 单个行人
    :param direction: 移动方向
    :return: None
    '''
    if direction == 0:
        p.x = p.x - 1
        p.y = p.y + 1
    elif direction == 1:
        p.y = p.y + 1
    elif direction == 2:
        p.x = p.x + 1
        p.y = p.y + 1
    elif direction == 3:
        p.x = p.x - 1
    elif direction == 4:
        p.x = p.x
    elif direction == 5:
        p.x = p.x + 1
    elif direction == 6:
        p.x = p.x - 1
        p.y = p.y - 1
    elif direction == 7:
        p.y = p.y - 1
    elif direction == 8:
        p.x = p.x + 1
        p.y = p.y - 1


def chickOverAround(p, allPeople):
    '''
    检测行人是否到达出口
    :param p: 单个行人
    :param allPeople: 所有行人
    :return: None
    '''
    if p.x >= Data.EXIT_X_LEFT and p.x <= Data.EXIT_X_RIGHT and p.y >= Data.ROOM_M:  # 如果行人到达出口
        # p.logo=Data.BasicData.LOGO_NULL
        allPeople.remove(p)  # 将该行人从行人列表移出
