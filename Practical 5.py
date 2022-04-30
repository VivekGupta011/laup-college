# write a program to do following

from calendar import c
from numpy import matrix


global r1,c1,r2,c2
# display M in matrix format
def printmatrix(A):
    for i in range(len(A)):
        print(A[i])

# matrix addition
def matrixadd(A,B):
   c=[[sum(A[i][j]+B[i][j] for j in range(len(B[0])))] for i in range (len(A))]
   print("Addition of matrix:")
   print(matrix(c))

# matrix multiplication
def matrixmul(A,B):
    c=[[sum(A[i][k]*B[k][j] for k in range (len(B)) for j in range (len(B[0])))]  for i in range (len(A))]
    
#matrix vector multiplication
def matrixvecmul(A,c):
    c=[sum(A[i][j]*V[j] for j in range (len(V))) for i in range(len(A))]
    print("matrix vector multiplication (M*V)=",c )

# vector matrix multiplication
def Vccmatrixmul(V,A):
    c=[sum V[j]*A[j][i] for j in range (len(V) for i in range(len(A)))]
    print("Vector of matrix mul (V*M)=",c)
