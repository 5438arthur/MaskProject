#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 22:08:32 2020

@author: arthuryang
"""
import time
import threading
a = 0
b = 0
    
def aloop():
    while True:
        global a 
         
        if a%2 == 0:
            print('a=',a)
            a+=2
            print(time.ctime(time.time()))
            time.sleep(2)
def bloop():
    while True:
        global b   
         
        if b%5 == 0:
            print('b=',b)
            b+=5
            print(time.ctime(time.time()))
            time.sleep(5)
        
        
threading.Thread(target=aloop).start()
threading.Thread(target=bloop).start()

#多執行緒執行結果
# a= 0 Sun Feb  9 23:57:21 2020
#         b= 0 Sun Feb  9 23:57:21 2020
# a= 2 Sun Feb  9 23:57:23 2020
#         b= 5 Sun Feb  9 23:57:26 2020
# a= 6 Sun Feb  9 23:57:27 2020
# a= 8 Sun Feb  9 23:57:29 2020
#         b= 10 Sun Feb  9 23:57:31 2020
# a= 10 Sun Feb  9 23:57:31 2020
# a= 12 Sun Feb  9 23:57:33 2020
# a= 14 Sun Feb  9 23:57:35 2020
#         b= 15 Sun Feb  9 23:57:36 2020
# a= 16 Sun Feb  9 23:57:37 2020
# a= 18 Sun Feb  9 23:57:39 2020
#         b= 20 Sun Feb  9 23:57:41 2020

