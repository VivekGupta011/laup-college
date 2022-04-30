# write a  program to do following 
# 1.Enter a vector b and find the projection of b orthogonal to a given vector v
# 2.Find the projection of b orthogonal to a set of given vectors 

#projection_orthogonal
def dot(x,y):
    return sum([x[i]*y[i] for i in range(len(x))])
def scalar(a,v):
    return [a*v[i] for i in range(len(v))]
def sub(u,v):
    return [ u[i]-v[i] for i in range(len(v))]
def projalong(b,v):
    s=(dot(b,v)/dot(b,b) if dot(b,b)!=0 else 0)
    return scalar(s,v)
def proj_orthogonal(b,v):
    return sub(b,projalong(b,v))
print("orthogonal projection of b=[5,-5,2] on v=[8,-2,2] is ",proj_orthogonal([5,-5,2],[8,-2,2]))
def proj_orthogonalvector(b,s):
    for i in range (len(s)):
        v=s[i]
        b=proj_orthogonal(b,v)
    return (b)
print("orthogonal projection of b=[5,-5,2] on v=[8,-2,2] is ",proj_orthogonalvector([5,-5,2],[[8,-2,2],[0,3,3]]))

