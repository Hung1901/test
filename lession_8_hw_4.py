# -*- coding: utf-8 -*-
"""Lession 8 - HW 4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_gjAWEaWMneH1--oCVsq4MMGMhnm7Kjr
"""

#Bài 04. Viết chương trình lấy ra các phần tử key-value xuất hiện trong cả 2 dict
a = {
    1: 5,
    2: 15,
    3: 8,
    4: 25,
    5: 55
}
b = {
    6: 3,
    7: 4,
    8: 5,
    9: 6,
    10: 7
}
for key, value in a.items():
  print(key, value)
for key, value in b.items():
  print(key, value)