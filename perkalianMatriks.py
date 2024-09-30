import numpy as np

a = np.array(([1,2,3],
              [4,5,6],
              [7,8,9]))

b = np.ones([3,3])

#Perkalian Matriks
c = np.dot(a,b)

print(b)
print(c)

"""
output: 
[[ 3.  3.]
 [ 7.  7.]
 [11. 11.]]
 """