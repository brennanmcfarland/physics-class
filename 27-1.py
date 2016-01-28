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

def iterateX(xn,yn,dt):
    "iterate for x"
    print(xn+dt*yn)
    return xn+dt*yn
def iterateY(xn,yn,tn,R,w,dt):
    "iterate for y"
    #print(yn+dt*(xn-4*math.pow(xn,3)-.154*yn+R*math.cos(w)*tn))
    return yn+dt*(xn-4*math.pow(xn,3)-.154*yn+R*math.cos(w)*tn)
#HERE IS WHERE THE PROGRAM STARTS:

#iterate 100 times:
iterations = 50000

#give it our first x and y:
x = [.1]
v = [.1]

#give it our R, w and dt:
R = 0.1
w = 1.2199778
dt = (2*math.pi/w)/500

#for 300 iterations, find the next x and y by iterating:
for i in range(0,iterations):
    x.append(iterateX(x[i],v[i],dt))
    v.append(iterateY(x[i],v[i],dt*(i),R,w,dt))
xt, yt = [],[]
for i in range(4000,5000):
	xt.append(x[i])
	yt.append(v[i])

#plot the approximation:
plt.plot(xt,yt)
plt.show()
