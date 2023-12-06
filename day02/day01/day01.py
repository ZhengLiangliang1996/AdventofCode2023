#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
import os 

PATH = '/Users/liangliang/Desktop/AdventofCode2022/2023'

def read_txt(filename):
    with open(filename) as file:
        lines = file.read().split('\n')
         
    return lines 

def solution1():
    fn = os.path.join(PATH, 'day01', 'input.txt')
    l = read_txt(fn)
    sum_1 = 0
    for i in range(len(l)):
        first_digit, second_digit = -1, -1
        index, neg_index = 0, -1
        print(l[i])
        while index < len(l[i]):
            if first_digit == -1:
                if(l[i][index].isdigit()):
                    first_digit = int(l[i][index])
            
            if second_digit == -1:
                if(l[i][neg_index].isdigit()):
                    second_digit = int(l[i][neg_index])
            if first_digit != -1 and second_digit != -1:
                sum_1 += first_digit * 10 + second_digit 
                print(first_digit, second_digit)
                break
            
            index += 1
            neg_index -= 1

    print(sum_1)
        
def solution2():
    fn = os.path.join(PATH, 'day01', 'input_2.txt')
    l = read_txt(fn)
    sum_1 = 0
    d = {'one':1, 'two':2, 'three':3, 
         'four':4, 'five':5, 'six':6, 
         'seven':7, 'eight':8, 'nine':9}
    
    for i in range(len(l)):
        first_digit, second_digit = -1, -1
        index, neg_index = 0, len(l[i])-1
        print(l[i])
        while index < len(l[i]):

            if first_digit == -1:
                if(not l[i][index].isdigit()):
                    if l[i][index:index+3] in d.keys():
                        first_digit = int(d[l[i][index:index+3]])
                    elif l[i][index:index+4] in d.keys():
                        first_digit = int(d[l[i][index:index+4]])
                    elif l[i][index:index+5] in d.keys():
                        first_digit = int(d[l[i][index:index+5]])

                if(l[i][index].isdigit()):
                    first_digit = int(l[i][index])

            
            if second_digit == -1:

                if(not l[i][neg_index].isdigit()):
                    if l[i][neg_index-3+1:neg_index+1] in d.keys():
                        second_digit = int(d[l[i][neg_index-3+1:neg_index+1]])
                    elif l[i][neg_index-4+1:neg_index+1] in d.keys():
                        second_digit = int(d[l[i][neg_index-4+1:neg_index+1]])
                    elif l[i][neg_index-5+1:neg_index+1] in d.keys():
                        second_digit = int(d[l[i][neg_index-5+1:neg_index+1]])

                if(l[i][neg_index].isdigit()):
                    second_digit = int(l[i][neg_index])

            if first_digit != -1 and second_digit != -1:
                sum_1 += first_digit * 10 + second_digit 
                print(first_digit, second_digit)
                break
            
            index += 1
            neg_index -= 1
        print(sum_1)


solution2()

