#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 21:56:39 2020

@author: arthuryang
"""

# 引入 requests 模組
import requests
import re

# 使用 GET 方式下載普通網頁
r = requests.get ('https://raw.githubusercontent.com/kiang/pharmacies/master/raw/maskdata.csv?fbclid=IwAR0pbpNYAtC4juY8ewEuYq6NyFBUcfLX65_qjxYiqqIl6SFn0xi9VP4DhUI')

#print(r.text)
#'\n' in r.text

lenall = len(r.text.split('\n')) - 2 #全部去前後（最後一行空白）

"""
#測試抓取
colcount=0
for rowcount in range (1,6):  #1~lenall(3144)
    for column in range (0,7):    
        print(re.split(',|\n',r.text)[colcount])  #原print(r.text.split(',')[colcount],'/') 效果不佳，改為用re
        colcount = colcount+1
    print('\n')
"""
dict1={} #縣市字典



for rowcount in range (1,2):  #先取五筆
    # print(re.split('縣|市|鄉|區',(re.split(',|\n',r.text)[2+7*rowcount])))
    temp = re.split('縣|市|鄉|區',(re.split(',|\n',r.text)[2+7*rowcount])) #地址切段 temp[0]=縣市 temp[1]=鄉鎮 temp[2]=其他剩餘
    #temp[0] = {temp[2] :re.split(',|\n',r.text)[1+7*rowcount]}
    #if temp[0] not in dict1: #縣市不在縣市字典中執行
    #    dict1[temp[0]] = eval(str(temp[0])) #建立縣市索引

 #本想以字典的值再建立字典，暫時卡住跳過       
        
    
    
    
