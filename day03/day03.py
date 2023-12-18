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


def check_surrounding(m, i, j_s, j_e):
    s = [1, 0, -1]
    coor = list(product(s, s))
    res = []
    found = False 
    gear = False 
    for j in range(j_s, j_e):
        for (xx, yy) in coor:
            x = i + xx
            y = j + yy
            if x>=0 and x<len(m) and y>=0 and y<len(m[0]):
                if not m[x][y].isdigit() and m[x][y] != '.':
                    found = True 
                if m[x][y] == '*':
                    gear = (x, y)
    return found, gear

def solution1():
    fn = os.path.join(PATH, 'day03', 'input.txt')
    l = read_txt(fn)
    m = []
    for i in range(len(l)-1):
        m.append(list(l[i])) 
    s = 0
    for i in range(len(m)):
        j = 0
        while j < len(m[0]):
            if l[i][j].isdigit(): 
                num = 0
                j_s = j
                while j < len(m[0]) and l[i][j].isdigit():
                    num = 10*num + int(l[i][j])
                    j += 1 
                j_e = j
               
                found, _ = check_surrounding(m, i, j_s, j_e)
                if num and found:
                    s += num
            else:
                j += 1
    print(s)

def solution2():
    fn = os.path.join(PATH, 'day03', 'input_2.txt')
    l = read_txt(fn)
    m = []
    for i in range(len(l)-1):
        m.append(list(l[i])) 
    s = 0
    gears = defaultdict(list)
    for i in range(len(m)):
        j = 0
        while j < len(m[0]):
            if l[i][j].isdigit(): 
                num = 0
                j_s = j
                while j < len(m[0]) and l[i][j].isdigit():
                    num = 10*num + int(l[i][j])
                    j += 1 
                j_e = j
                
                found, gear = check_surrounding(m, i, j_s, j_e)
                if num and found:
                    gears[gear].append(num)
            else:
                j += 1

    for k, v in gears.items():
        if len(v) == 2:
            print(v[0], v[1])
            s += v[0] * v[1]
    
    print(s)

solution2()

