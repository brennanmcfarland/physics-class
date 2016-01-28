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

def iterateX(xn,yn,zn,a,b,c,dt):
    "iterate for x"
    return xn+a*(yn-xn)*dt
def iterateY(xn,yn,zn,a,b,c,dt):
    "iterate for y"
    return yn+(-yn+b*xn-xn*zn)*dt
def iterateZ(xn,yn,zn,a,b,c,dt):
	return zn+(-c*zn+xn*yn)*dt
#HERE IS WHERE THE PROGRAM STARTS:

#iterate 400 times:
iterations = 400

#create our list of n integers and configure the axes:
n = list(range(0,iterations+1))
#plt.axis([0,len(n)-1,0,1])

#give it our initial variables:
x = [0]
y = [10]
z = [0]
dt = .01
a = 10
b = 28
c = 8/3

#for 100 iterations, find the next x and y by iterating:
for i in range(0,iterations):
    x.append(iterateX(x[i],y[i],z[i],a,b,c,dt))
    y.append(iterateY(x[i],y[i],z[i],a,b,c,dt))
    z.append(iterateZ(x[i],y[i],z[i],a,b,c,dt))

#plot the approximation:
plt.plot(x,y)

#reset variables
x = [0]
y = [11]
z = [0]
dt = .01
a = 10
b = 28
c = 8/3

#for 100 iterations, find the next x and y by iterating:
for i in range(0,iterations):
    x.append(iterateX(x[i],y[i],z[i],a,b,c,dt))
    y.append(iterateY(x[i],y[i],z[i],a,b,c,dt))
    z.append(iterateZ(x[i],y[i],z[i],a,b,c,dt))

#plot the approximation:
plt.plot(x,y)

plt.show()