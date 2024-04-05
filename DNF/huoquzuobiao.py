import os
import threading

import cv2

import numpy as  np
wupin_zuobiao =[]
guaiwu_zuobiao =[]


def huoqu_juese_zuobiao(datupian_huidu):
    xiaotupian  = cv2.imread('juese.png')
    xiaotupian_huidu = cv2.cvtColor(xiaotupian,cv2.COLOR_BGR2GRAY)


    # 在大图片中查找小图片

    result = cv2.matchTemplate(datupian_huidu,xiaotupian_huidu,cv2.TM_CCOEFF_NORMED)

    # 筛选结果

    locations = np.where(result >=0.85)
    locations = list(zip(*locations[::-1]))

    if len(locations) > 0:
        return (locations[0][0],locations[0][1]+140)
    return (0,0)


def chazhao_tupian(datupian_huidu,xiaotupian_huidu,xiaotupianmengcheng):
    global guaiwu_zuobiao
    result = cv2.matchTemplate(datupian_huidu,xiaotupian_huidu,cv2.TM_CCOEFF_NORMED)

    locations = np.where(result>=0.85)
    locations = list(zip(*locations[::-1]))

    if len(locations)>0:
        print(locations)
        for location in locations:
            mingcheng_xinxi =xiaotupianmengcheng.split("_") # 将小图片的名称按—分割，获取图片的类型
            xiuzheng_x = mingcheng_xinxi[1]
            xiuzheng_y = mingcheng_xinxi[2]
             # 将查找图片的坐标加上修正后的坐标，加上图片裁切的高度
            guaiwu_zuobiao.append((location[0]  + int (xiuzheng_x),location[1] + 130 + int(xiuzheng_y)))

def huoqu_guaiwu_zuobiao(datupian_huidu):
     global guaiwu_zuobiao
     guaiwu_zuobiao =[]
     xiaotupian_liebiao =os.listdir('guaiwu/')

     datupian_huidu = datupian_huidu[130:535,0:799]

     # 定义一个线程组

     threads = []

     for xiaotupian_mingcheng in xiaotupian_liebiao:
         xiaotupian = cv2.imread('guaiwu/' + xiaotupian_mingcheng)
         xiaotupian_huidu = cv2.cvtColor(xiaotupian,cv2.COLOR_BGR2GRAY)


         # 创建线程并启动

         thread = threading.Thread(target=chazhao_tupian,args=(datupian_huidu,xiaotupian_huidu,xiaotupian_mingcheng))
         thread.start()
         threads.append(thread)


         #等待所有线程完成
     for thread in threads:
         thread.join()


     return guaiwu_zuobiao


# 获取 boss坐标
def huoqu_boss_zuobiao(datupian_huidu):
    datupian_huidu = datupian_huidu[130:535,0:799]

    xiaotupian =cv2.imread('boss.png')
    xiaotupian_huidu = cv2.cvtColor(xiaotupian,cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(datupian_huidu,xiaotupian_huidu,cv2.TM_CCOEFF_NORMED)

    # 筛选结果
    locations = np.where(result>=0.85) # 用np筛选一下高于0.85的结果
    locations = list(zip(*locations[::-1])) # 将结果再次处理一下，仅保留坐标值

    if len(locations)>0:
        return [(locations[0][0],locations[0][1]+130+300)]
    return []

# 获取物品坐标

def chazhao_wupin_tupian(datupian_huidu,xiaotupian_huidu,xiaotupian_mingcheng):
    global wupin_zuobiao

    result = cv2.matchTemplate(datupian_huidu,xiaotupian_huidu,cv2.TM_CCOEFF_NORMED)

    # 筛选结果

    locations = np.where(result>=0.85)
    locations = list(zip(*locations[::-1]))
    if len(locations)>0:
        print(locations)
        for location in locations:
            mingcheng_xinxi = xiaotupian_mingcheng.split("_")
            xiuzheng_x = mingcheng_xinxi[1]
            xiuzheng_y = mingcheng_xinxi[2]
            wupin_zuobiao.append((location[0]+int(xiuzheng_x),location[1]+300+int(xiuzheng_y)))


def huoqu_wupin_zuobiao(datupian_huidu):
    global wupin_zuobiao
    wupin_zuobiao=[]
    xiaotupian_liebiao = os.listdir('wupin/')

    datupian_huidu = datupian_huidu[300:535,0:799]

    # 定义一个线程组
    threads = []

    for xiaotupian_mingcheng in xiaotupian_liebiao:
        xiaotupian = cv2.imread('wupin/'+ xiaotupian_mingcheng)
        xiaotupian_huidu =cv2.cvtColor(xiaotupian,cv2.COLOR_BGR2GRAY)


        # 创建线程组并启动

        thread = threading.Thread(target=chazhao_wupin_tupian,args=(datupian_huidu,xiaotupian_huidu,xiaotupian_mingcheng))
        thread.start()
        threads.append(thread)

        # 等待所有线程完成
        for thread in threads:
            thread.join()

        return wupin_zuobiao


# 获取门坐标

def chazhao_men_tupian(datupian_huidu,xiaptupian_huidu,xiaotupian_mingcheng):
    global  men_zuobiao

    result = cv2.matchTemplate(datupian_huidu,xiaptupian_huidu,cv2.TM_CCOEFF_NORMED)

    # 筛选结果

    locations = np.where(result>=0.85)
    locations = list(zip(*locations[::-1]))
    if len(locations)>0:
        print(locations)
        for location in locations:
            mingcheng_xinxi = xiaotupian_mingcheng.split("_")# 将小图片的名称按-分割，获取图片类型
            xiuzheng_x = mingcheng_xinxi[1]
            xiuzheng_y =mingcheng_xinxi[2]
            men_zuobiao.append((location[0]+int(xiuzheng_x),location[1]+130 + int(xiuzheng_y)))

def huoqu_men_zuobiao(datupian_huidu):
    global men_zuobiao

    men_zuobiao = []

    xiaotupian_liebiao = os.listdir('men/')


    datupian_huidu = datupian_huidu[130:535,0:799]


    # 定义一个线程组

    threads = []

    for xiaotupian_mingcheng in xiaotupian_liebiao:
        xiaotupian = cv2.imread('men/'+ xiaotupian_mingcheng)
        xiaotupian_huidu = cv2.cvtColor(xiaotupian,cv2.COLOR_BGR2GRAY)


        # 创建线程并启动

        thread = threading.Thread(target=chazhao_men_tupian,args=(datupian_huidu,xiaotupian_huidu,xiaotupian_mingcheng))
        thread.start()
        threads.append(thread)

        # 等待所有线程完成

        for thread in threads:
            thread.join()

        return men_zuobiao

