## -*- coding: UTF-8 -*-

# Filename : jahaka
# author by : sylzhenshuai
import random
print('\n----华丽分割线 练习一 ----')
a=float(input('输入三角形的第一边长a=: '))
b=float(input('输入三角形的第二边长b=: '))
c=float(input('输入三角形的第三边长c=: '))




if (a+b>c) and(a+c>b) and (b+c>a):
    if(abs(a-b)>=c)or(abs(b-c)>=a)or(abs(a-c)>=b):
        print("错误，某两边之差大于第三边，所以无法组成三角形")
    else:
        if(a==b)or(b==c)or(a==c):
            print('正确，可以组成等边或等腰三角形')
        else:
            print('正确，可以组成不等边三角形')
else:
    print("错误，某两边之和小于第三边，所以无法组成三角形")
