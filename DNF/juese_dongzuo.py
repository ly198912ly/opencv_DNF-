import time
import jianpanshubiao


# 定义几个方向的变量 ，记录按键是否按下，为了避免冲突 我们在前面加了一个x或者y

x_left = 0
x_right =0
y_up =0
y_down =0 # juexing_jineng 是一个列表，包含一个字典元素
juexing_jineng = [{'anjian':'9', 'shifang_shijian':0, 'Lengque':8, 'shichang':1.5}]

# 字典的内容解释如下：
# 'anjian':'9',        # 按键的标识，值为'9'
# 'shifang_shijian':0, # 释放时间，值为 0
# 'Lengque':8,         # 冷却时间，值为 8
# 'shichang':1.5       # 持续时间，值为 1.5



putong_jineng=[{'anjian':'j','shifang_shijian':0, 'lengque':5, 'shichang':0.5},
{'anjian': 'k','shifang_shijian':0, 'Lengque':2.9, 'shichang':0.4},
{'anjian': 'L', 'shifang_shijian':0, 'lengque':6, 'shichang':0.4},
{'anjian':';', 'shifang_shijian':0, 'lengque':5.8, 'shichang':0.4},
{'anjian': '7', 'shifang_shijian':0, 'Lengque':5, 'shichang':0.4},
{'anjian':'8', 'shifang_shijian':0, 'Lengque':3.9, 'shichang':0.4}, ]

juexing_jineng = [{'anjian':'9', 'shifang_shijian':0, 'Lengque':8, 'shichang':1.5}]


# 移动方法

def yidong(juese_zuobiao,mubiao_zuobiao):
    global x_left,x_right,y_up,y_down

    # x 轴的方向逻辑
    # 检查角色和目标在x坐标上的距离是否大于等于10
    if abs(juese_zuobiao[0]-mubiao_zuobiao[0])>=10: # 如果角色在目标的右边，即角色的x坐标大于目标的x坐标
        if juese_zuobiao[0] - mubiao_zuobiao[0]>0:  # 如果之前的移动方向是向右（也就是x_right=1，即右键被按下），现在需要角色向左移动，所以释放右键，按下左键。
            if x_right==1:
                time.sleep(0.01)
                jianpanshubiao.keyUp('x_right')
                x_right=0
            if x_left ==1:
                pass
            elif x_left==0:
                if abs(juese_zuobiao[0]-mubiao_zuobiao[0])>80:
                    time.sleep(0.01)
                    jianpanshubiao.press('a')
                    time.sleep(0.05)
                time.sleep(0.01)
                jianpanshubiao.keyDown('a')
                x_left=1
        elif juese_zuobiao[0]-mubiao_zuobiao[0]<0:
            if x_left == 1:
                time.sleep(0.01)
                juese_zuobiao.keyUp('a')
                x_left=0
            if x_right==1:
                pass
            elif x_right==0:
                if abs(juese_zuobiao[0]-mubiao_zuobiao[0])>80:
                    time.sleep(0.01)
                    jianpanshubiao.press('d')
                    time.sleep(0.01)
                    juese_zuobiao.keyDown('d')
                    x_right=1

    else:
        if x_right==1:
            time.sleep(0.01)
            juese_zuobiao.keyUp('d')
            x_right=0

        if x_left==1:
            time.sleep(0.01)
            juese_zuobiao.keyUp('a')
            x_left=0

    # y轴方向逻辑

    if abs(juese_zuobiao[1]- mubiao_zuobiao[1])>=5:
        if juese_zuobiao[1]-mubiao_zuobiao[1]>0:
            if y_down==1:
                time.sleep(0.01)
                jianpanshubiao.keyUp('s')
                y_down=0
            if y_up==1:
                pass
            elif y_up==0:
                time.sleep(0.01)
                jianpanshubiao.keyDown('w')
                y_up=1
        elif juese_zuobiao[1]-mubiao_zuobiao[1]<0:
            if y_up==1:
                time.sleep(0.01)
                juese_zuobiao.keyUp('w')
                y_up=0
            if y_down==1:
                pass
            elif y_down==0:
                time.sleep(0.01)
                juese_zuobiao.keyDown('s')
                y_down=1

    else:
        if y_down==1:
            time.sleep(0.01)
            juese_zuobiao.keyUp('s')
            y_down=0
        if y_up==1:
            time.sleep(0.01)
            jianpanshubiao.keyUp('w')
            y_up=0

# 停止的方法

def tingzhi():      # 定义一个名为tingzhi的函数
    global x_left,x_right,y_up,y_down  # 声明全局变量x_left,x_right,y_up,y_down
    jianpanshubiao.fuwei()    # 调用jianpanshubiao模块的fuwei函数
    if x_left==1:             # 如果全局变量x_left等于1
        x_left=0              # 则将其设为0
    if x_right==1:            # 如果全局变量x_right等于1
        x_right=0             # 则将其设为0
    if y_up==1:               # 如果全局变量y_up等于1
        y_up=0                # 则将其设为0
    if y_down==1:             # 如果全局变量y_down等于1
        y_down=0              # 则将其设为0


# 攻击怪物方法
def gongji_guaiwu(gongji_fangxiang):
    shifang_jing_geshu = 0 # 记录是否释放了技能

    time .sleep(0.01)
    jianpanshubiao.press(gongji_fangxiang)
    time.sleep(0.01)

    for jineng in putong_jineng:
        if (time.time()-jineng['shifang_shijian'])>jineng['lengque']:
            jianpanshubiao.press(jineng['anjian'])
            time.sleep(0.05)
            jineng['shifang_shijian'] = time.time()
            shifang_jineng_geshu =shifang_jing_geshu + 1
            time.sleep(jineng['shichang'])

        if shifang_jineng_geshu >= 1:
                break
    if shifang_jineng_geshu == 0:
            time.sleep(0.01)
            jianpanshubiao.press('x')
            time.sleep(0.1)
            jianpanshubiao.press('x')
            time.sleep(0.1)
            jianpanshubiao.press('x')
            time.sleep(0.1)
# 攻击boss方法

def dongji_boss(gongji_fangxiang):
    shifang_jineng_geshu = 0 # 记录是否释放了技能

    time.sleep(0.01)
    jianpanshubiao.press(gongji_fangxiang)
    time.sleep(0.01)

    for juexing in juexing_jineng:
        if (time.time() - juexing['shifang_shijian']) > juexing['lengque']:
            jianpanshubiao.press(juexing['anjian'])
            time.sleep(0.05)
            juexing['shifang_shijian'] = time.time()
            time.sleep(juexing['shichang'])
            # time.sleep(0.5)#间隔0.5秒再次释放其他的技能,

    for jineng in putong_jineng:
        if (time.time() - jineng['shifang_shijian']) > jineng['lengque']:
            jianpanshubiao.press(jineng['anjian'])
            time.sleep(0.05)
            jineng['shifang_shijian'] = time.time()
            shifang_jineng_geshu = shifang_jineng_geshu + 1
            time.sleep(jineng['shichang'])
            # time.sleep(0.5)#间隔0.5秒再次释放其他的技能,
        if  shifang_jineng_geshu >= 1:
                break



    if shifang_jineng_geshu == 0:
        time.sleep(0.01)
        jianpanshubiao.press('h')
        time.sleep(0.1)
        jianpanshubiao.press('h')
        time.sleep(0.1)
        jianpanshubiao.press('h')
        time.sleep(0.1)


