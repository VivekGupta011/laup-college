# write a program which demonstrate the following
# 1.addition of two complex number
# 2.Displaying the conjugate of a complex number
# 3.plotting a set of complex numbers
# 4.creating a new plot by rotating the given number by 90,180 and 270 degree and also by scaling by a number a=1/2,a=1/3 and a=2 etc

import matplotlib.pyplot as plt
# addition of the two complex number hiii vivek
a=29+7j
b=10-2j
c=a+b
print("Real number:",a.real)
print("Imaginary number:",a.imag)
print()
print("Adition of the two complex number is ",c)
print()
# display the conjugate of acomplex number 
print("Original complex number:",a)
print("conjugate of a complex number:",a.conjugate())
print()
# plotting a set of a complex numbers
s={3+3j,2+1j,5+1j,4+3j}
print("s:",s)
x=[x.real for x in s]
y=[x.imag for x in s]
plt.plot(x,y,'go')  #where g means green color & o means circle symbol
plt.axis([-6,6,-6,6])
plt.show()


