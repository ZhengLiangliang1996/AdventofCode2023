#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
import os 
import re

PATH = '/Users/liangliang/Desktop/AdventofCode2022/2023'

def read_txt(filename):
    with open(filename) as file:
        lines = file.read().split('\n')
         
    return lines 

def solution1():
    fn = os.path.join(PATH, 'day02', 'input.txt')
    l = read_txt(fn)
    sum_1 = 0
    d_clr_max = {'red':12, 'green':13, 'blue':14}
    number_match = '(\d+)'
    game_sum, game_regex = 5050, r'Game (\d+):'
    for i in range(len(l)):
        game_num = 0
        match = re.match(game_regex, l[i])
        game_num = int(match.groups()[0])
        possible = 1
        for sets in l[i].split(";"):
            print(sets)
            if not possible:
                break
            for key in d_clr_max.keys():
                    
                match = re.search(f" (\d+) {key}" ,sets)
                if match:
                    if int(match.groups()[0]) > d_clr_max[key]:
                        print(sets)
                        print(f'{game_num} not possible')
                        game_sum -= game_num
                        possible = 0
                        break

        print(game_sum)


def solution2():
    fn = os.path.join(PATH, 'day02', 'input_2.txt')
    l = read_txt(fn)
    sum_1 = 0
    d_clr_max = {'red':12, 'green':13, 'blue':14}
    game_sum = 0
    for i in range(len(l)):
        game_num = 0
        red, blue, green = 0, 0, 0 
        print(l[i])
        for sets in l[i].split(";"):
            for key in d_clr_max.keys():
                match = re.search(f" (\d+) {key}",sets)
                if match:
                    num = int(match.groups()[0]) 
                    if key == 'red':
                        red = max(red, num)
                    elif key == 'green':
                        green = max(green, num)
                    elif key == 'blue':
                        blue = max(blue, num)
        print(red, green, blue)
        game_sum += red * green * blue
        print(game_sum)


solution2()

