# -*- coding: utf-8 -*-
"""Lession 8 - HW 7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lAC2D-63AmpU36ZSQXkR_qcKqpXnd6jc
"""

#Bài 07. Viết hàm đếm số lần xuất hiện các ký tự trong một String
s = 'Stringings'
count={}
for i in s:
    if i in count:
        count[i] +=1
    else:
        count[i] = 1
 
print(count)