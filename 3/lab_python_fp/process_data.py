#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import sys
from print_result import print_result
from unique import Unique
from field import field
from gen_random import gen_random
from cm_timer import cm_timer_1
# Сделаем другие необходимые импорты

path = sys.argv[1]

# Необходимо в переменную path сохранить путь к файлу, который был передан при запуске сценария

with open(path) as f:
    data = json.load(f)

# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк

@print_result
def f1(arg):
    return sorted(Unique(field(arg, "job-name")))


@print_result
def f2(arg):
    return list(filter(lambda x: (str)(x).startswith("программист"), arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + " с опытом Python", arg))


@print_result
def f4(arg):
    joined = zip(arg, gen_random(len(arg), 100000, 200000))
    for i in joined:
        yield "{}, с зарплатой {} руб.".format(i[0], i[1])


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))