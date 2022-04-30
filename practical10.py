#using sympy
import sympy
M=sympy.Matrix([[3,-2],[1,0]])
print(M)
print("Eigen Values of M =",M.eigenvals())
print("Eigen Vectors of M =",M.eigenvects())