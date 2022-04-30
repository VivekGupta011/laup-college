# write code for following
# find the GCD of 2 given numbers using Eculids algorithm
# Enter a positive number N and find a & b such that a^2-b^2=N


# 1
a=int(input("Enter first number:"))
b=int(input("Enter Second number:"))
def GCD(a,b):
    if b==0:
        return(a)
    else:
        return(GCD(b,a%b))
print("GCD is:",GCD(a,b))


# 2
N=int(input("Enter n:"))
def check(a,b,n):
    if (a*a)-(b*b)==n:
        print("a is =",a,"b is =",b)
for i in range(0,N+1):
    for j in range(0,N+1):
        check(i,j,N)


    
