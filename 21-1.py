import matplotlib.pyplot as plt
import math

def graphfunction(xmin,xmax,xres,function,*args):
    "takes a given mathematical function and graphs it-how it works is not important"
    x,y = [],[]
    i=0
    while xmin+i*xres<=xmax:
        x.append(xmin+i*xres)
        y.append(function(x[i],*args))
        i+=1
    return [x,y]

def k1x(xn,yn,w,dt):
	return w*yn*dt
def k1y(xn,yn,w,dt):
	return -w*xn*dt
def k2x(xn,yn,w,dt):
	return w*(yn+.5*k1y(xn,yn,w,dt))*dt
def k2y(xn,yn,w,dt):
	return -w*(xn+.5*k1x(xn,yn,w,dt))*dt
def k3x(xn,yn,w,dt):
	return w*(yn+.5*k2y(xn,yn,w,dt))*dt
def k3y(xn,yn,w,dt):
	return -w*(xn+.5*k2x(xn,yn,w,dt))*dt
def k4x(xn,yn,w,dt):
	return w*(yn+k3y(xn,yn,w,dt))*dt
def k4y(xn,yn,w,dt):
	return -w*(xn+k3x(xn,yn,w,dt))*dt

def euleriterateX(xn,yn,a,b):
    return 1+yn-a*xn*xn
def euleriterateY(xn,yn,a,b):
    return xn*b
def iterateX(xn,yn,w,dt):
    "iterate for x"
    return xn+k1x(xn,yn,w,dt)/6+k2x(xn,yn,w,dt)/3+k3x(xn,yn,w,dt)/3+k4x(xn,yn,w,dt)/6
def iterateY(xn,yn,w,dt):
    "iterate for y"
    return yn+k1y(xn,yn,w,dt)/6+k2y(xn,yn,w,dt)/3+k3y(xn,yn,w,dt)/3+k4y(xn,yn,w,dt)/6
#HERE IS WHERE THE PROGRAM STARTS:

#iterate 100 times:
iterations = 100

#create our list of n integers and configure the axes:
n = list(range(0,iterations+1))
#plt.axis([0,len(n)-1,0,1])

#give it our first x and y:
x = [1]
y = [1]

#give it our w and dt:
w = 1
dt = .1

#for 300 iterations, find the next x and y by iterating:
for i in range(0,iterations):
    x.append(iterateX(x[i],y[i],w,dt))
    y.append(iterateY(x[i],y[i],w,dt))

#plot the approximation:
plt.plot(n,x)
plt.show()