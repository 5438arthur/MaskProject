#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 21:05:05 2020

@author: arthuryang
"""
#優化
#以位移值搜遍所有地址，找到完全符合者，再印出相關資料

# 引入 requests 模組
import requests
import re



def GetInfo():
    global allinfo 
    r = requests.get ('https://raw.githubusercontent.com/kiang/pharmacies/master/raw/maskdata.csv?fbclid=IwAR0pbpNYAtC4juY8ewEuYq6NyFBUcfLX65_qjxYiqqIl6SFn0xi9VP4DhUI')
    allinfo = list(re.split(',|\n|\r',r.text))
    
def FindInfo():
    global lenall
    #總共要抓的數量
    lenall = int((len(allinfo)-1)/8)-2 #全部去前後（最後一行空白）
   
    locate = '桃園市八德區' # input (' ')
    
    
    for rowcount in range (1,lenall):  #先取五筆
        bool = re.match(locate,allinfo[2+7*rowcount])
        if bool:
            print('詳細地址',allinfo[2+7*rowcount],'\n')
            print('醫院名稱',allinfo[1+7*rowcount],'\n')
            print('電話',allinfo[3+7*rowcount],'\n')
            print('成人口罩剩餘',allinfo[4+7*rowcount],'\n')
            print('小孩口罩剩餘',allinfo[5+7*rowcount],'\n')
            
    
GetInfo()
FindInfo()
print(lenall)