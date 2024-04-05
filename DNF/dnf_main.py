import time

import mss
import cv2
import numpy as np
import jianpanshubiao
import panduanchangjing
import huoquzuobiao
import dixiacheng

# 定义要捕捉区域，固定写法
quyu = {"left": 0, "top": 0, "width": 800, "height": 600}
mubiao_zuobiao=[]
guaiwu_zuobiao = []
boss_huobiao = []

with mss.mss() as sct:
    while True:
        changjing = '未知'
        juese_zuobiao = (0, 0)

        quyujieping = sct.grab(quyu)
        quyujieping = np.array(quyujieping)

        datupian_huidu = cv2.cvtColor(quyujieping, cv2.COLOR_BGR2GRAY)

        juese_zuobiao = huoquzuobiao.huoqu_juese_zuobiao(datupian_huidu)
        print('角色坐标为:', juese_zuobiao)

        # 判断场景
        changjing = panduanchangjing.panduanchangjing(datupian_huidu)
        print('当前画面在', changjing)

        if changjing == '地下城':
            dixiacheng.dixiacheng(datupian_huidu,juese_zuobiao)






        # 画出怪物的方框
        if len(dixiacheng.guaiwu_zuobiao) > 0:
            for i in guaiwu_zuobiao:
                cv2.rectangle(quyujieping, (i[0] - 10, i[1] - 50), (i[0] + 10, i[1]), (0, 0, 255), 2)

        # 画出boss方框
        if len(dixiacheng.boss_zuobiao) > 0:
            for i in dixiacheng.boss_zuobiao:
                cv2.rectangle(quyujieping, (i[0] - 10, i[1] - 50), (i[0] + 10, i[1]), (0, 0, 255), 5)


        # 画出物品方框

        if len(dixiacheng.wupin_zuobiao) > 0:
            for i in dixiacheng.wupin_zuobiao:
                cv2.rectangle(quyujieping, (i[0] - 10, i[1] - 10), (i[0] + 10, i[1]), (0, 255, 0), 2)



        # 画出门方框

        if len(dixiacheng.men_zuobiao) > 0:
            for i in dixiacheng.men_zuobiao:
                cv2.rectangle(quyujieping, (i[0] - 10, i[1] - 10), (i[0] + 10, i[1]), (255, 255, 255), 2)


        # 画出目标的方框

        if len(dixiacheng.mubiao_zuobiao)>0:
            cv2.rectangle(quyujieping,(dixiacheng.mubiao_zuobiao[0]-20,dixiacheng.mubiao_zuobiao[1]-50),
            (dixiacheng.mubiao_zuobiao[0]+20,dixiacheng.mubiao_zuobiao[1]),(0,255,255),2)

        cv2.imshow("DNF", quyujieping)
        if cv2.waitKey(5) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            jianpanshubiao.fuwei()
            break