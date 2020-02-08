#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 23:29:18 2020

@author: arthuryang
"""

#以位移值搜遍所有地址，找到完全符合者，再印出相關資料

# 引入 requests 模組
import requests
import re

# 使用 GET 方式下載普通網頁
r = requests.get ('https://raw.githubusercontent.com/kiang/pharmacies/master/raw/maskdata.csv?fbclid=IwAR0pbpNYAtC4juY8ewEuYq6NyFBUcfLX65_qjxYiqqIl6SFn0xi9VP4DhUI')

#總共要抓的數量
lenall = len(r.text.split('\n')) - 2 #全部去前後（最後一行空白）


locate = '桃園市八德區' # input (' ')


for rowcount in range (1,lenall):  #先取五筆
    bool = re.match(locate,re.split(',|\n',r.text)[2+7*rowcount])
    if bool:
        print('詳細地址',re.split(',|\n',r.text)[2+7*rowcount],'\n')
        print('醫院名稱',re.split(',|\n',r.text)[1+7*rowcount],'\n')
        print('電話',re.split(',|\n',r.text)[3+7*rowcount],'\n')
        print('成人口罩剩餘',re.split(',|\n',r.text)[4+7*rowcount],'\n')
        print('小孩口罩剩餘',re.split(',|\n',r.text)[5+7*rowcount],'\n')
    
    
    
    #temp = re.split('縣|市|鄉|區',(re.split(',|\n',r.text)[2+7*rowcount])) #地址切段 temp[0]=縣市 temp[1]=鄉鎮 temp[2]=其他剩餘
    #temp[0] = {temp[2] :re.split(',|\n',r.text)[1+7*rowcount]}
    #if temp[0] not in dict1: #縣市不在縣市字典中執行
    #    dict1[temp[0]] = eval(str(temp[0])) #建立縣市索引