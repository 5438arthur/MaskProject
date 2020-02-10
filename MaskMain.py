#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 22:24:29 2020

@author: arthuryang
"""

import PostLocationReverse
import DataToDict6


 
#抓所有口罩資料
DataToDict6.GetInfo() 




#郵遞區號轉位置
zipcode = input('請輸入郵遞區號 ')
(location1,location2)=PostLocationReverse.ZipcodeToLocation(zipcode) 
location=location1+location2

#以位置查詢資料
DataToDict6.SearchInfo(location)

 


