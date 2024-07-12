import numpy as np
import math

# problem 1
a = np.array([1,2,3])
b = np.array([4,5,6])

sum = a+b
difference = a-b
print("\nproblem 1")
print(f"sum of vectors: {sum}")
print(f"Difference of vectors: {difference}")

#problem 2
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

sum_matrix = A +B
difference_matrix = A-B
print("\nproblem 2")
print(f"Sum of matrix: {sum_matrix}")
print(f"Difference of matrix: {difference_matrix}")

#problem 3
dot_product = np.dot(a,b)
print("\nproblem 3")
print(f"Dot product of vectors: {dot_product}")


#problem 4
A2 = np.array([[1,2,3],[4,5,6]])
B2 = np.array([[7,8,9,10],[11,12,13,14],[15,16,17,18]])

product_matrix = np.dot(A2,B2)
print("\nproblem 4")
print(f"product of matrix: {product_matrix}")

#problem 5
a2 = np.array([1,1,2])

magnitude = np.linalg.norm(a2)
print("\nproblem 5")
print(f"magnitude of vector: {magnitude}")

#problem 6
transpose = A.T
print("\nproblem 6")
print(f"transpose matrix: {transpose}")