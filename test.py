from algebra import *

m = [[2, -1, 3, 9],
     [1, 1, 1, 6],
     [1, -1, 1, 2]]

a = [[1,2,3],
     [4,5,6],
     [7,8,9]]

b = [[9,8,7],
     [6,5,4],
     [3,2,1]]

c = [[1,2,-1],
     [-2,0,1],
     [1,-1,0]]

print('x,y,z=',cramer(m))

print(cofactor(a))

print(f'Cofactor of a_{0},{0} ',cofactor_of_element(a,0,0))

print("a * b = ",mult(a,b))

print("a / b = ", div([[4,5,7],
                       [2,1,0],
                       [1,2,3]], [[1,1,1],
                                  [2,3,4],
                                  [3,1,1]]))

print("inverse of c = ",inverse(c))

print("Adjoint of a = ",adjoint(a))

print("Eigenvalues = ",eigenvalues([[2,1],
                   [1,2]]))