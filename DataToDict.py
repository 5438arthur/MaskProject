#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 02:56:14 2020

@author: arthuryang
"""
# 引入 requests 模組
import requests
import re

# 使用 GET 方式下載普通網頁
r = requests.get ('https://raw.githubusercontent.com/kiang/pharmacies/master/raw/maskdata.csv?fbclid=IwAR0pbpNYAtC4juY8ewEuYq6NyFBUcfLX65_qjxYiqqIl6SFn0xi9VP4DhUI')

#print(r.text)
#'\n' in r.text

lenall = len(r.text.split('\n')) - 2

#for row in range (1,lenall+1):  #1~lenall(3144)
#    for column in range (0,6):    #0~5
#        print(r.text.split(',')[column],'\n')



colcount=0
for rowcount in range (1,6):  
    for column in range (0,7):    
        print(r.text.split(',')[colcount],'/')
        colcount = colcount+1
    #print('\n')
