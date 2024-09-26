import numpy as np

a = np.array([1,2,3,4,5])
b = np.array([1.5 , 2.5 , 3.5 , 4.5 , 5.5])

#membuat vector dengan range
c = np.arange(1,10,1.5)
#start, stop, step
print(c)
"""
output
[1.  2.5 4.  5.5 7.  8.5]
"""


#membuat linspace
d = np.linspace(1,10,4)
# print(d)
"""
output
[ 1.  4.  7. 10.]
"""


#array multidimensi / matriks
e = np.array([(1,2,3),(4,5,6)])
# print(e)

"""
output
[[1 2 3]
 [4 5 6]]
"""

#matiks dengan nilai nol
f = np.zeros((5,5))
# print(f)
"""
output :
 [[0. 0. 0. 0. 0.]
  [0. 0. 0. 0. 0.]
  [0. 0. 0. 0. 0.]
  [0. 0. 0. 0. 0.]
  [0. 0. 0. 0. 0.]]
"""

#matriks dengan nilai 1
g = np.ones((5,5))
# print(g)

""" 
output
[[1. 1. 1. 1. 1.]
[1. 1. 1. 1. 1.]
[1. 1. 1. 1. 1.]
[1. 1. 1. 1. 1.]
[1. 1. 1. 1. 1.]]
""" 
 
#matiks identitas
h1 = np.identity(5)
# print(h1)

"""
output: 
[[1. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0.]
 [0. 0. 1. 0. 0.]
 [0. 0. 0. 1. 0.]
 [0. 0. 0. 0. 1.]]
"""

h2 = np.eye(5)
# print(h2)

"""output
[[1. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0.]
 [0. 0. 1. 0. 0.]
 [0. 0. 0. 1. 0.]
 [0. 0. 0. 0. 1.]]
"""