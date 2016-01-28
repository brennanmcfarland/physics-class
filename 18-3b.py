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

def iterateX(xn,yn,cr):
    "iterate for x"
    return xn*xn-yn*yn+cr
def iterateY(xn,yn,ci):
    "iterate for y"
    return 2*xn*yn+ci
#HERE IS WHERE THE PROGRAM STARTS:

#iterate 100 times:
iterations = 20

#create our list of n integers and configure the axes:
n = list(range(0,iterations+1))
#plt.axis([0,len(n)-1,0,1])

#give it our initial variables:
x = [0]
y = [0]
cr = -1
ci = 0

#for 100 iterations, find the next x and y by iterating:
for i in range(0,iterations):
    x.append(iterateX(x[i],y[i],cr))
    y.append(iterateY(x[i],y[i],ci))

#plot the approximation:
plt.plot(x,y)

plt.show()