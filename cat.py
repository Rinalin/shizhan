#!/user/bin/env python
# -*- coding:utf-8 -*-
from shizhan.animal import Animal


class Cat(Animal):
    def __init__(self,name,color,age,sex,hair):
        super().__init__(name,color,age,sex)
        self.hair = hair

    def cache(self):
        print('我会抓老鼠')

    def shout(self):
        print('我会喵喵叫')

if __name__=='__main__':
    xiaoke = Cat('小可','black','5','female','long')
    xiaoke.cache()
    xiaoke.shout()

