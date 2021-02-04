#!/user/bin/env python
# -*- coding:utf-8 -*-
class Animal:
    def __init__(self,name,color,age,sex):
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex

    def shout(self):
        print('我会叫')

    def run(self):
        print('我会跑')

if __name__=='__main__':
    little_mikkey = Animal()
