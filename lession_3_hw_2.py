# -*- coding: utf-8 -*-
"""Lession 3 - HW 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1R-yQRFkau363cofmPjenDVvEbr8Eozqm
"""

#Bài 02. Lập chương trình tính các tổng sau:
#    S_1 = 1 + x + x^2 + x^3 + ... + x^n
#    S_2 = 1 - x + x^2 - x^3 + ... + (-1)^n.x^n
#    S_3 = 1 + x/1! + x^2/2! + ... + x^n/n!
#Trong đó, n là số nguyên dương và x là một số thực bất kì. Cả 2 đều được nhập từ bàn phím

# S_1
n = int(input('Nhập n ='))
while n >= 0:
  x = float(input('Nhập x ='))
  S_1 = 0
  i = 0
  for i in range(0, n+1):
    S_1 = S_1 + x**i
    print(f'Tổng = {S_1}')

# S_2
n = int(input('Nhập n ='))
while n >= 0:
  x = float(input('Nhập x ='))
  S_2 = 0
  i = 0
  for i in range(0, n+2):
    S_2 = S_2 + (-x**i)
    print(f'Tổng = {S_2}')

# S_3
import math
n = int(input('Nhập n ='))
while n >= 0:
  x = float(input('Nhập x ='))
  S_3 = 0
  i = 0
  for i in range(0, n+1):
    S_3 = S_3 + x**i/math.factorial(i)
    print(f'Tổng = {S_3}')