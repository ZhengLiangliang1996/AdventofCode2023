#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
import os 
import re
from itertools import product
from collections import defaultdict

PATH = '/Users/liangliang/Desktop/AdventofCode2023'

def read_txt(filename):
    with open(filename) as file:
        lines = file.read().split('\n')
         
    return lines 

def solution1():
    fn = os.path.join(PATH, 'day04', 'input.txt')
    l = read_txt(fn)
    s = 0
    for i in range(len(l)-1):
        p1 = l[i].split(':')[1].split('|')
        l1 = list(map(int, p1[0].strip().split()))
        l2 = list(map(int, p1[1].strip().split()))
        a = set(l1).intersection(set(l2))
        if len(a) >= 1:
            s += 2**(len(a)-1)
    print(s)

def solution2():
    fn = os.path.join(PATH, 'day04', 'input.txt')
    l = read_txt(fn)
    for i in range(len(l)-1):
        p1 = l[i].split(':')[1].split('|')
        l1 = list(map(int, p1[0].strip().split()))
        l2 = list(map(int, p1[1].strip().split()))
        a = set(l1).intersection(set(l2))
        if len(a) >= 1:
            s += 2**(len(a)-1)
    print(s)

solution1()

