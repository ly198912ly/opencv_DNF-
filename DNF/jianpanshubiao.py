import serial

import time

# 配置串口参数

ser = serial.Serial('COM3',baudrate=9600,timeout=0.2)


# 定义一个按键码 用来字符和实际控制码的转换
anjianma={
    'up':'52',
    'down':'51',
    'left':'50',
    'right':'4F',
    'w':'1A',
    'a':'04',
    's':'16',
    'd':'07',

}
# 发送串口数据
def fasong(data):
    data_str = ''.join(data)
    hex_data =bytes.fromhex(data_str)
    ser.write(hex_data)
    time.sleep(0.05)

# 定义一个计算效验码的函数
def jisuan_sum(datalist):
    total_sum = 0
    for data in datalist:
        total_sum+= int(data,16)

    sum = hex(total_sum)[-2:]
    return sum


#定义一个按下的函数,用于按下某个按键,我们这里没有控制键的需求,就不考虑这个了
def anxia(anjian):
    #他盘命令的前缀,这部分不会发生变化
    datalist=["57", "AB", "00", "02", "08", "00", "00"]

    #组合按下的按键
    datalist.append(anjianma[anjian])
    datalist.append("00")
    datalist.append("00")
    datalist.append("00")
    datalist.append("00")
    datalist.append("00")

    #计算效验码
    xiaoyanma = jisuan_sum(datalist)

    #组合完整的命令
    datalist.append(xiaoyanma)

    #发送
    fasong(datalist)

#弹起按键
def tanqi(anjian):
    datalist = ["57", "AB", "00", "02", "08", "00", "00", "00", "00", "00", "00", "00", "00", "OC"]
    # 发送
    fasong(datalist)


def fuwei():
    pass


