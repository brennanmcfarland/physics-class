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

def iterateX(xn,yn,w,dt):
    "iterate for x"
    return xn+w*yn*dt
def iterateY(xn,yn,w,dt):
    "iterate for y"
    return yn-w*xn*dt
#HERE IS WHERE THE PROGRAM STARTS:

#iterate 300 times:
iterations = 300

#create our list of n integers and configure the axes:
n = list(range(0,iterations+1))
#plt.axis([0,len(n)-1,0,1])

#give it our first x and y:
x = [0]
y = [1.0]

#give it our w and dt:
w = 1
dt = .05

#for 300 iterations, find the next x and y by iterating:
for i in range(0,iterations):
    y.append(iterateY(x[i],y[i],w,dt))
    x.append(iterateX(x[i],y[i],w,dt))

#plot the approximation:
plt.plot(list(range(0,iterations+1)),y)

#reset x and y:
x = [0]
y = [1.1]

#for 300 iterations, find the next x and y by iterating:
for i in range(0,iterations):
    y.append(iterateY(x[i],y[i],w,dt))
    x.append(iterateX(x[i],y[i],w,dt))
plt.plot(list(range(0,iterations+1)),x)
plt.show()
