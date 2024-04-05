import cv2

import numpy as np

# 注意优先级问题

changjingliebiao = ['dixiacheng.png','juesexuanze.png','sailiya.png','chengzheng.png']


def panduanchangjing(datupian_huidu):

    # 判断场景
    for  i in changjingliebiao:
        # 获取小图片

        xiaotupian =cv2.imread(i)
        xiaotupian_huidu = cv2.cvtColor(xiaotupian,cv2.COLOR_BGR2GRAY)

        # 在大图片中查找小图片
        result = cv2.matchTemplate(datupian_huidu,xiaotupian_huidu,cv2.TM_CCOEFF_NORMED)

        # 筛选结果

        locations = np.where(result >= 0.85) # 用np筛选一下结果高于0.85的

        locations = list(zip(*locations[::-1])) # 将结果再次处理一下。仅保留坐标值

        if len(locations) > 0:
            if 'juesexuanze'  in i:
                return "角色选择"

            elif 'sailiya' in i:
                return "赛利亚"

            elif 'chengzhen' in i:
                return "城镇"

            elif 'dixiacheng' in i:
                return "地下城"

            break

    return "未知场景"






