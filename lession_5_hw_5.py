# -*- coding: utf-8 -*-
"""Lession 5 - HW 5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JXmDAfjTmXJdAEdaDOMXE9d5oDNwHGy_
"""

#Bài 05. Viết chương trình in ra các ký tự số trong chuỗi được nhập từ bàn phím
s = input('Chuỗi bất kỳ: ')
for c in s:
  if '0' <= c <= '9':
    print(c)

s = input('Chuỗi bất kỳ: ')
for i in range(0, len(s)):
  if '0' <= s[i] <= '9':
    print(s[i])