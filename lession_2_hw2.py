# -*- coding: utf-8 -*-
"""Lession 2-HW2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1B5_mNcq02AZv0FzpkXtpFX_KibHgPwbU
"""

import math
x = int(input('Số bất kỳ'))
y = int(input('Số bất kỳ'))
z = int(input('Số bất kỳ'))
F = (x+y+z)/(x**2+y**2+1)-(x-z*math.cos(y))
print(f'Giá trị của F là: {F}')