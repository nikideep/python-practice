# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#importing libraries
def split_and_join(line):
    # write your code here
    line = line.split(" ")
    line = "-".join(line)
    return lineth



if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
