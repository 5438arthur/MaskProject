#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 01:52:16 2020

@author: arthuryang
"""

#優化
#以位移值搜遍所有地址，找到完全符合者，再印出相關資料

# 引入 requests 模組
#import requests
import re
import requests
import time
import threading
import MaskMain

def GetInfo():
    global allinfo 
    r = requests.get ('https://raw.githubusercontent.com/kiang/pharmacies/master/raw/maskdata.csv?fbclid=IwAR0pbpNYAtC4juY8ewEuYq6NyFBUcfLX65_qjxYiqqIl6SFn0xi9VP4DhUI')
    allinfo = list(re.split(',|\n|\r',r.text))
    #time.sleep(300)
    
def SearchInfo(location):
    #location = MaskMain.location #測試用
    global lenall
    #總共要抓的數量
    lenall = int((len(allinfo)-1)/8)-2 #全部去前後（最後一行空白）
   
    locate=location # input (' ')
    
    
    for rowcount in range (1,lenall):  #先取五筆
        if MaskMain.Printstate == 'Done'or'Start': 
            bool = re.match(locate,allinfo[2+7*rowcount])
            if bool:
                address = (allinfo[2+7*rowcount])
                name = (allinfo[1+7*rowcount])
                phone = (allinfo[3+7*rowcount])
                adult = (allinfo[4+7*rowcount])
                child = (allinfo[5+7*rowcount])
                return(address,name,phone,adult,child)
                MaskMain.Printstate = 'NotYet'
            else:
                global Datastate
                Datastate = 'Done'
            
#threading.Thread(target = GetInfo).start()
#threading.Thread(target = FindInfo).start()
