import huoquzuobiao
import juese_dongzuo
guaiwu_zuobiao =[]
boss_zuobiao =[]
wupin_zuobiao=[]
men_zuobiao =[]

mubiao_leixing =''
mubiao_zuobiao=[]



def dixiacheng(datupian_huidu,juese_zuobiao):
    # 初始化变量
    global guaiwu_zuobiao,boss_zuobiao,wupin_zzuobiao,men_zuobiao
    global   mubiao_leixing,mubiao_zuobiao

    guaiwu_zuobiao =[]
    boss_zuobiao = []
    wupin_zuobiao = []
    men_zuobiao = []
    mubiao_leixing = ''
    mubiao_zuobiao = []

    guaiwu_zuobiao = huoquzuobiao.huoqu_guaiwu_zuobiao(datupian_huidu)

    boss_zuobiao = huoquzuobiao.huoqu_boss_zuobiao(datupian_huidu)

    wupin_zzuobiao = huoquzuobiao.huoqu_wupin_zuobiao(datupian_huidu)

    men_zuobiao = huoquzuobiao.huoqu_men_zuobiao(datupian_huidu)


    # 如果有boss，目标就是boss
    if len(boss_zuobiao)>0:
        mubiao_leixing ='boss'
        mubiao_zuobiao=boss_zuobiao[0]
    # 如果有怪物，但是没有物品
    elif len(guaiwu_zuobiao)>0 and len(wupin_zuobiao)==0:
        mubiao_leixing='guaiwu'
        mubiao_zuobiao=zuijin_zuobiao(guaiwu_zuobiao,juese_zuobiao)

        # 如果有怪物，也有物品，则比较2者和角色的距离，如果怪物较远，则先拾取物品
    elif len(guaiwu_zuobiao)>0 and len(wupin_zuobiao)>0:
        zuijin_guaiwu =zuijin_zuobiao(guaiwu_zuobiao,juese_zuobiao)
        zuijin_wupin = zuijin_zuobiao(wupin_zuobiao,juese_zuobiao)
        guaiwu_juli =abs(juese_zuobiao[0]-zuijin_guaiwu[0])+abs(juese_zuobiao[1]-zuijin_guaiwu)
        wupin_juli = abs(juese_zuobiao[0]-zuijin_wupin[0])+abs(juese_zuobiao[1]-zuijin_wupin[1])

        if wupin_juli<guaiwu_juli and abs(wupin_juli - guaiwu_juli)>150:
            mubiao_leixing = 'wupin'
            mubiao_zuobiao = zuijin_wupin

        else:
            mubiao_leixing ='guaiwu'
            mubiao_zuobiao = zuijin_guaiwu

    elif len(guaiwu_zuobiao)==0 and len(wupin_zuobiao)>0:
        mubiao_leixing ='wupin'
        mubiao_zuobiao = zuijin_zuobiao(wupin_zuobiao,juese_zuobiao)
    elif len(men_zuobiao)>0:
        mubiao_leixing ='men'



    else:
        mubiao_leixing =''
        mubiao_zuobiao=[]

    print('当前目标为',mubiao_zuobiao)

    # 根据目标做出动作
    if mubiao_leixing=='boss':
        if abs(juese_zuobiao[1]-mubiao_zuobiao[1])<=20 and abs(juese_zuobiao[0]-mubiao_zuobiao[0])<=200:
            dongzuo = '攻击boss'
            print('攻击boss')
            juese_dongzuo.tingzhi()
            if juese_dongzuo[0]-mubiao_zuobiao[0]>0:
                #juese_dongzuo.gongji_boss('a')
                pass
                # 攻击boss左
            else:
                #juese_dongzuo.gongji_boss('d')
                pass
                # 攻击boss左

        else:
            dongzuo = '移动到boss附近'
            print('移动到boss附近')
            juese_dongzuo.yidong(juese_zuobiao,mubiao_zuobiao)


        # 目标是怪物
    elif mubiao_leixing =='guaiwu':
        if abs(juese_zuobiao[1]-mubiao_zuobiao[1])<=20 and abs(juese_zuobiao[0]-mubiao_zuobiao[0])<=200:
            print('攻击怪物')
            juese_dongzuo.tingzhi()
            if juese_zuobiao[0]-mubiao_zuobiao[0]>0:
                #juese_dongzuo.gongji_guaiwu('a')
                pass
                # 攻击怪物左
            else:
                #juese_dongzuo.gongji_guaiwu('d')
                pass
                # 攻击怪物右

        else:
            dongzuo = '移动到怪物附近'
            print('移动到怪物附近')
            juese_dongzuo.yidong(juese_zuobiao,mubiao_zuobiao)


        # 目标是物品

    elif mubiao_leixing=='wupin':
        if abs(juese_zuobiao[1] - mubiao_zuobiao[1])<=5 and abs(juese_zuobiao[0]-mubiao_zuobiao[0])<=0:
            print('捡东西')
            dongzuo = '捡东西'
            juese_dongzuo.tingzhi()
            #  捡东西


        else:
            print('移动到物品上')
            dongzuo = '移动到物品上'
            # 移动到物品坐标上
            juese_dongzuo.yidong(juese_zuobiao,mubiao_zuobiao)


        # 目标是门

    elif mubiao_leixing=='door':
        if abs(juese_zuobiao[1]-mubiao_zuobiao[1])<=10 and abs(juese_zuobiao[0]-mubiao_zuobiao[0])<=10:
            print('进门')
            dongzuo='进门'
            juese_dongzuo.tingzhi()
            # 移动到门坐标上


        else:
            print('移动到门里面')
            dongzuo = '移动到门里面'
            # 移动到门坐标上
            juese_dongzuo.yidong(juese_zuobiao,mubiao_zuobiao)

    elif mubiao_leixing=='':
        juese_dongzuo.tingzhi()







# 计算那个坐标离角色最近

def zuijin_zuobiao(coordinates_list,given_coordinate):
    # 初始化最小距离和对应的坐标
    min_distance =None
    zuijin_zuobiao =None


    # 计算曼哈顿距离并找到最近的坐标
    for coord in coordinates_list:
        x1,y1 =given_coordinate
        x2,y2 = coord
        distance =abs(x1 -x2)+abs(y1-y2)


        # 如果是第一个坐标或者距离更近，则更新最小距离和最近的坐标

        if min_distance is None or distance<min_distance:
            min_distance =distance
            zuijin_zuobiao = coord


    return zuijin_zuobiao



