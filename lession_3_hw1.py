# -*- coding: utf-8 -*-
"""Lession 3 - HW1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1g45OFbVLVgkn7MFWOfPwoEvev_Z-mejl
"""

# Bài tập 1: Giải phương trình bậc 2: ax^2 + bx + c = 0
import math
a = float(input('Nhập a ='))
b = float(input('Nhập b ='))
c = float(input('Nhập c ='))
d = b**2 - 4*a*c

if a == 0 or c == 0:
  if b == 0:
    print(f'Phương trinh vô nghiệm')
  else:
    print(f'Phương trình có 1 nghiệm x = {-c/b}')
else:
  if d > 0:
    x_1 = (-b + math.sqrt(d)/(2*a))
    x_2 = (-b - math.sqrt(d)/(2*a))
    print(f'Phương trình có 2 nghiệm x_1 = {x_1} và x_2 = {x_2}')
  elif d == 0:
    x = -b/(2*a)
    print(f'Phương trình có nghiệm kép x_1 = x_2 = {x}')
  else:
    print(f'Phương trình vô nghiệm')