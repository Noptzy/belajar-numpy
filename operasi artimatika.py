import numpy as np
import sys  

#list python
a = np.array([1,2,3,4,5])
b = np.array([6,7,8,9,10])

#Elementwise operation

#penjumblahan
hasil = a + b
"""
output :
[ 7  9 11 13 15]
"""

#pengurangan
hasil = a - b
"""
output :
[-5 -5 -5 -5 -5]
"""
 
#perkalian
hasil = a * b
"""
output :
[ 6 14 24 36 50]
""" 
 
#pembagian
hasil = a / b
"""
output :
[0.16666667 0.28571429 0.375      0.44444444 0.5       
"""

#kuadrat
hasil = a ** 2
"""
output:
[ 1  4  9 16 25]
"""


#multidimensi array numpy
c = np.array([[1,2,3],[4,5,6]])
d = np.array([[7,8,9],[-1,-2,-3]])

hasil = c + d
"""
output: 
[[ 8 10 12]
 [ 3  3  3]]
"""

print(hasil)