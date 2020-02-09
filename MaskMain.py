#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 22:24:29 2020

@author: arthuryang
"""

import PostLocationReverse
import DataToDict6

def PrintAndBack():
    print(address,name,phone,adult,child)
    global Printstate
    Printstate ='Done'

Printstate ='Start'  
#PostLocationReverse
zipcode = input('請輸入郵遞區號 ')
(location1,location2)=PostLocationReverse.ZipcodeToLocation(zipcode) 
location=location1+location2


DataToDict6.GetInfo()
(address,name,phone,adult,child)=DataToDict6.SearchInfo(location)
    
while DataToDict6.Datastate != 'Done':
    PrintAndBack()

