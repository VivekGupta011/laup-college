import matplotlib.pyplot as plt
print("Ploating for 180 degree")
print("Original set s")
s={3+3j,2+1j,5+1j,4+3j}
print("s:",s)
s1={x*(-1) for x in s}
print()
print("s1:",s1)
x=[x.real for x in s1]
y=[y.imag for y in s1]
plt.plot(x,y,'bo')
plt.show()