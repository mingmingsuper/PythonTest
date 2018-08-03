#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
这是测试
"""

from types import MethodType
from Student import Student
from Cate import Cate
from Chain import Chain
import json
from Animal import Animal
from collections import namedtuple
from Building import Building
from Unit import Unit

__author__ = 'LiuMingMing'

# print ("Hello, World!")
# name = raw_input('请输入您的姓名：')
# print("hello " + name + ",你好")
# print(r'\\\\\t')
# print('''first line
#        second line
#        third line''')
#
# print(ord('A'))
#
# print(chr(65))

# 定义带参数函数病检查数据类型
# def my_abs(x):
#     if not isinstance(x, (int, float)):
#         raise TypeError('bad type')
#
#     if x > 0:
#         return x
#     else:
#         return -x
#
#
# def calc(*numbers):
#     sum = 0
#     for num in numbers:
#         sum = sum + num * num
#     return sum
#
#
# print(my_abs(-10))
#
# print(calc(1, 2, 3, 4, 5))

import functools


# 定义带可变参数函数
def func1(a: int, b: int, *kw: int) -> object:
    print(a, b, kw),


func1(1, 1, 2, 4, 3)


# 关键字参数函数定义
def func2(a: int, b: int, **param):
    print(a, b, param)


func2(1, 1, name="jack", age=100)

import os

a = [d for d in os.listdir('.')]
print(a)


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5


o = odd()

next(o)

next(o)

next(o)

# next(o)


L = [('Bob', 75), ('Adam', 92), ('bart', 66), ('Lisa', 88)]

S = sorted(L, key=lambda tup: (tup[0].lower()), reverse=True)
print(S)


def log(func):
    def wrapper(*args, **kw):
        print("call %s():" % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    print("2018-07-31")


now()


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print("call %s():" % func.__name__)
        return func(*args, **kw)

    return wrapper


max2 = functools.partial(max, 10)

print(max2(*(10, 5, 6, 7)))

animal = Animal('cate')

student = Student('jack', 100, 10, animal)

student2 = Student('jack', 100, 50, animal)

student.print_score()

student.say_hello()

cate = Cate('bob')
cate.run()
cate.eat()

print(dir(cate))

# def set_age(self, age):
#     self.age = age


# student.name = "Lucy"
# student.sex = '男'
student.age = 90
print(student.age)
print(student2.age)
print(student)
# print(student.name)


# 动态绑定方法到实例
# student.set_age = MethodType(set_age, student)
# student.set_age(20)
# print(student.age)

url1 = Chain().users.test
print(url1)

url = Chain().users('mac').photo('testphoto').repos

print(url)


# 使用type创建class
def fn(self, name='world'):
    print('Hello, %s.' % name)


Hello = type('Hello', (object,), dict(hello=fn))
h = Hello()
h.hello('Mac')

with open('/Users/liumingming/Desktop/堆栈.txt', 'r') as f:
    # f.write('Hello world')
    print(f.read())

building = Building('来福士', Unit('number one'), ['1', '2', '3'])

building_json = json.dumps(building, default=lambda obj: obj.__dict__)
print('Dump Student:', building_json)

building_obj = json.loads(building_json, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
print(building_obj.unit.name)
