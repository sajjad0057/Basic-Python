from pylab import *

A=5
f = 100
nCyl = 5
fs = 100 * f
t = arange(0, nCyl * 1 / f, 1 / fs)
y=A*sin(2*pi*f*t)
plot(t,y)
grid()
show()