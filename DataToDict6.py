#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 01:52:16 2020

@author: arthuryang
"""



import re
import requests



def GetInfo():
    global allinfo 
    r = requests.get ('https://raw.githubusercontent.com/kiang/pharmacies/master/raw/maskdata.csv?fbclid=IwAR0pbpNYAtC4juY8ewEuYq6NyFBUcfLX65_qjxYiqqIl6SFn0xi9VP4DhUI')
    allinfo = list(re.split(',|\n|\r',r.text))
    
    
def SearchInfo(location):
    global lenall
    #總共要抓的數量
    lenall = int((len(allinfo)-1)/8)-2 #全部去前後（因為第一行是標題，最後一行是空白）
      
    for rowcount in range (1,lenall):  #一列一列取
        bool = re.match(location,allinfo[2+8*rowcount])
        if bool:
            address = (allinfo[2+8*rowcount])
            name = (allinfo[1+8*rowcount])
            phone = (allinfo[3+8*rowcount])
            adult = (allinfo[4+8*rowcount])
            child = (allinfo[5+8*rowcount])
            print(address,name,phone,adult,child)
    print(allinfo[14])
            

