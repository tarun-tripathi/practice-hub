# Q8a: NumPy Matrix Operations and Circuit Solver
# Task: Perform matrix operations and solve an electrical circuit using Ohm's law
# Concept: V = IR, solve system of equations using numpy.linalg.solve
# Docs: https://numpy.org/doc/stable/reference/routines.linalg.html

import numpy as np

print("=== Matrix Operations ===")

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

print("Matrix A:")
print(A)
print("
Matrix B:")
print(B)
print("
A + B:")
print(A + B)
print("
A * B (element-wise):")
print(A * B)
print("
A dot B (matrix multiply):")
print(np.dot(A, B))
print("
Transpose of A:")
print(A.T)

print("
=== Circuit Solver (Ohm's Law) ===")
# Two loop circuit:
# Loop 1: R1*I1 + R2*(I1-I2) = V1
# Loop 2: R2*(I2-I1) + R3*I2 = V2
# Rearranged:
# (R1+R2)*I1 - R2*I2 = V1
# -R2*I1 + (R2+R3)*I2 = V2

R1, R2, R3 = 5, 10, 15
V1, V2 = 20, 10

R = np.array([[R1 + R2, -R2],
              [-R2, R2 + R3]])
V = np.array([V1, V2])

I = np.linalg.solve(R, V)
print(f"R1={R1}, R2={R2}, R3={R3}")
print(f"V1={V1}V, V2={V2}V")
print(f"Current I1 = {I[0]:.4f} A")
print(f"Current I2 = {I[1]:.4f} A")