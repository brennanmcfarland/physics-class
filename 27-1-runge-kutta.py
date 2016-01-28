import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import math

def iterateX(xn,yn):
    "iterate for x"
    print(xn+dt*yn)
    return xn+dt*yn
def iterateY(xn,yn):
    "iterate for y"
    #print(yn+dt*(xn-4*math.pow(xn,3)-.154*yn+R*math.cos(w)*t))
    return yn+dt*(xn-4*math.pow(xn,3)-.154*yn+R*math.cos(w*t))
 
def rungekutta(xn,yn):
	k1x = dt*yn
	k1y = dt*(xn-A*pow(xn,3)-B*yn+R*math.cos(w*t))
	k2x = dt*(yn+.5*k1y)
	k2y = dt*(xn+.5*k1x-A*math.pow(xn+.5*k1x,3)
			-B*(yn+.5*k1y)+R*math.cos(w*(t+.5*dt)))
	k3x = dt*(yn+.5*k2y)
	k3y = dt*(xn+.5*k2x-A*math.pow(xn+.5*k2x,3)
			-B*(yn+.5*k2y)+R*math.cos(w*(t+.5*dt)))
	k4x = dt*(yn+k3y)
	k4y = dt*(xn+k3x-A*pow(xn+k3x,3)-B*(yn+k3y)+R*math.cos(w*(t+dt)))
	return [k1x/6.0+k2x/3.0+k3x/3.0+k4x/6.0+xn,
			k1y/6.0+k2y/3.0+k3y/3.0+k4y/6.0+yn]

periods = 1
w = 1.2199778
T = 2*math.pi/w
A = 4.0
B = .154
k = -1
dt = T/1000
R = .11209725
t = 0.0
x = [.01]
v = [.01]

for i in range(0,periods):
	for j in range(0,200000):
		x.append(iterateX(x[j],v[j]))
		v.append(iterateY(x[j],v[j]))
		#if(i == periods-1) and (j%50 == 0):
		if(j%10 == 0):
			print("X: ",x[j]," V: ",v[j], "t: ",t)
		t = t + dt
xplot = []
vplot = []

i=len(x)-16*(int)(T/dt)
while(i<len(x)):
	xplot.append(x[i])
	vplot.append(v[i])
	t = t + dt
	i = i + 1
plt.plot(xplot,vplot)
plt.show()