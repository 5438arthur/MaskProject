#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 22:24:29 2020

@author: arthuryang
"""

# 引入 requests 模組
import requests
# 引入 Beautiful Soup 模組
from bs4 import BeautifulSoup

# 使用 GET 方式下載普通網頁
#r = requests.get ('https://l.facebook.com/l.php?u=https%3A%2F%2Fraw.githubusercontent.com%2Fkiang%2Fpharmacies%2Fmaster%2Fraw%2Fmaskdata.csv%3Ffbclid%3DIwAR0pbpNYAtC4juY8ewEuYq6NyFBUcfLX65_qjxYiqqIl6SFn0xi9VP4DhUI&h=AT2KUnBP4GVz6k07GxNA90dFodulJ1wTzq1AJLA66E367I_v_UHYRxviHkJWNVgprS-gZlt0zVPicCN0w4awkeOrI8ZUOR5V-tiLC590n9CzV7-PKhqe_tNyE7tkuUluf3Y5_qqLmHk')
r = requests.get ('https://raw.githubusercontent.com/kiang/pharmacies/master/raw/maskdata.csv?fbclid=IwAR0pbpNYAtC4juY8ewEuYq6NyFBUcfLX65_qjxYiqqIl6SFn0xi9VP4DhUI')

# 伺服器回應的狀態碼
# print(r.status_code)

# 輸出網頁 HTML 原始碼
print(r.text)

# 以 Beautiful Soup 解析 HTML 程式碼
#soup = BeautifulSoup(r.text, 'html.parser')

# 輸出排版後的 HTML 程式碼
#print(soup.prettify())