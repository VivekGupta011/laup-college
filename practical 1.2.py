# plotting as a 90 degree
import matplotlib.pyplot as plt
s={6+3j,2+7j,5+9j,4+3j}
print("S:",s)
s1={x*(1j) for x in s}
x=[x.real for x in s1]
y=[y.imag for y in s1]
plt.plot(x,y,'bo')
plt.show()

