# -*- coding: utf-8 -*-
"""Lession 9 - HW 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19LlmecRYVqrWcLlIfShThQ2JzDhI0TbZ
"""

#Bài 02. Viết hàm
#        def reverse_string(str)
#    trả lại chuỗi đảo ngược của chuỗi str

def reverse_string(str):
  return str[::-1]


x = reverse_string('Xin chào mọi người')
print(x)