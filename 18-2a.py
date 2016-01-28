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

def iterateX(xn,yn,a,b):
    "iterate for x"
    return 1+yn-a*xn*xn
def iterateY(xn,yn,a,b):
    "iterate for y"
    return b*xn
#HERE IS WHERE THE PROGRAM STARTS:

#iterate 100 times:
iterations = 10

#create our list of n integers and configure the axes:
n = list(range(0,iterations+1))
#plt.axis([0,len(n)-1,0,1])

#give it our initial variables:
x = [0]
y = [0]
a = .1
b = .3

#for 100 iterations, find the next x and y by iterating:
for i in range(0,iterations):
    x.append(iterateX(x[i],y[i],a,b))
    y.append(iterateY(x[i],y[i],a,b))

#plot the approximation:
plt.plot(x,y)

plt.show()