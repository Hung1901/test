# -*- coding: utf-8 -*-
"""Lession 9 - HW 5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KP8vvJpQMq400mE8oMHVel5E8sMY6ek_
"""

#Bài 05. Viết hàm
#        def count_upper_lower(str)
#    trả lại số lượng chữ cái viết hoa, số lượng chữ cái viết thường trong chuỗi str
def count_upper_lower(str):
    count_upper = 0
    count_lower = 0
    for c in str:
        if c.isupper():
            count_upper += 1
        if c.islower():
            count_lower += 1

    print("Số lượng chữ viết Hoa =", count_upper)
    print("Số lượng chữ viết thường =", count_lower)


str = input('Nhập chuỗi:')
count_upper_lower(str)