# -*- coding: utf-8 -*-
"""Lession 5 - HW 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ENyYWMowouv2SboOVIVLUTlNuDe9D-_z
"""

#Bài tập 2: Viết chương trình sinh ra một chuỗi từ 2 ký tự đầu và 2 ký tự cuối trong chuỗi được nhập vào, nếu độ dài chuỗi nhỏ hơn 2 thì in ra chuỗi rỗng.
s = input('Nhập chuỗi bất kỳ = ')
if len(s) > 2:
  print(f's_1 = {s[0:2]+s[-2:]}')
else:
  print('""')