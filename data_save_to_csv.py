#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   data_save_to_csv.py
@Time    :   2020/04/14 14:55:58
@Author  :   望 
@Version :   1.0
@Contact :   2521664384@qq.com
@Desc    :   None
'''

# here put the import lib

import csv


def test():
    with open('weibo.csv','w') as csvfile:
        fieldnames = ['id','name','age']
        writer = csv.DictWriter(csvfile,fieldnames = fieldnames)
        writer.writeheader
        writer.writerow({'id':1,'name':'小强','age':22})
        writer.writerow({'id':1,'name':'小强','age':22})

def save_main_information(main_info):
    with open('weibo.csv','a') as csvfile:
        fieldnames = ['love','comment','forward','time','main_information']
        writer = csv.DictWriter(csvfile,fieldnames = fieldnames)
        writer.writeheader
        writer.writerow(main_info)

def save_personal_information(personal_info):
    with open('weibo_person.csv','a') as csvfile:
        fieldnames = ['昵称','简介','注册时间','阳光信用','关注:','被关注:']
        writer = csv.DictWriter(csvfile,fieldnames = fieldnames)
        writer.writeheader
        writer.writerow(personal_info)

if __name__ == "__main__":
    test()
    save_main_information()