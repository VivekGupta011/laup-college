# write a program to do the following 
# 1. enter a vector u as a n-list
# 2. enter another vector v as a n-list
# 3.find the vector au+bu for different values of and b
# 4.find the dot product of u and v   

def addvec(x,y):
    return[x[i]+y[i] for i in range (len(x))]
def subvec(x,y):
    return[x[i]-y[i] for i in range (len(x))]

def dotprod(x,y):
    return sum([x[i]*y[i] for i in range(len(x))])                                                                                            

def scalarmul(x,p):
    return [p*x[i] for i in range(len(x))]

u=[]
v=[]
n=int(input("Enter the length of the vectors;"))
print("Enter the elements of vector u:")
for i in range(n):
    elem=int(input("Enter elements:"))
    u.append(elem)
print("Vector u:",u)
print("enter the elements of vector v:")
for i in range (n):
    elem=int(input("Enter element:"))
    v.append(elem)
print("vector v:",v)
print("Adition of vectors u and v is",addvec(u,v))
print("Subtraction of vectors u and v is ",subvec(u,v)) 
# au+bv
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))

print("scalar multiplication of a with u is au",scalarmul(u,a))
print("Scalar multiplication of b with v is bv",scalarmul(v,b))
print("The value of au+bv is",addvec(scalarmul(u,a),scalarmul(v,b)))
# dot product
print("Dot product of u and v is",dotprod(u,v))

