## -*- coding: UTF-8 -*-

# Filename : jahaka
# author by : sylzhenshuai
#导入随机数模块
import random
# 打印开头

#print('小学数学卷')
#用‘w’方式新建一个结果文件
filename = "小学数学卷.text"

f = open(filename, 'w')  # write 方式第一次写一行

text2write = "---开始出题目---\n"
f.write(text2write)
f.close()


#用‘a’方式打开文件，准备追加数学题
#指定要读的文件名
filename = "小学数学卷.text"
f=open(filename,'a')#append方式读文件
# 计数器，累加所出题目个数
count=0
#要产生n行n列的输出

for row in range(1,21):
    line1 = ''
    for col in range(1,6):
        count = count + 1
        #随机生成两个0到99之间的整数

        a = random.randint(0,99)

        b = random.randint(0,99)

        #随机生成运算符
        op =random.randint(1,4)

        #当op=1是加法的时候
        if op == 1:
            line1 = line1 + "%d+%d =\t" %(a,b)
            #print(line1)
        #    print('第{0}行，第{1}列第{2}题\t\t\t'.format(row,col,count))
        #当op=2是减法的时候
        if op == 2:
            line1 = line1 + "%d-%d =\t" %(a,b)
            #print(line1)
        #当op=3是乘法的时候
        if op == 3:
            line1 = line1 + "%d*%d =\t" %(a,b)
            #print(line1)
        #当op=4是除法的时候
        if op == 4:
            line1 = line1 + "%d/%d =\t" %(a,b)
            #print(line1)
    #print(line1)
    text2write= line1+'\n'
    f.write(text2write)
#    print("\n")







#打印结尾

text2write="总共出了{0}道数学题\n".format(count)
f.write(text2write)

f.close()
