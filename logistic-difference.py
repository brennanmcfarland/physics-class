import matplotlib.pyplot as plt

def graphfunction(xmin,xmax,xres,function,*args):
    "takes a given mathematical function and graphs it-how it works is not important"
    x,y = [],[]
    i=0
    while xmin+i*xres<=xmax:
        x.append(xmin+i*xres)
        y.append(function(x[i],*args))
        i+=1
    return [x,y]

def iterate(xn,R):
    "iterate the logistic difference equation"
    return R*xn*(1-xn)

#HERE IS WHERE THE PROGRAM STARTS:

#for our first graph, we need only iterate a few times
#to see convergence:
iterations = 5

#create our list of n integers and configure the axes:
n = list(range(0,iterations+1))
plt.axis([0,len(n)-1,0,1])

#give it our R and our first x, the first y is calculated:
R = 2.0
x = [.3]

#for 100 iterations, find the next x and y by iterating:
for i in range(0,iterations):
    x.append(iterate(x[i],R))

#annotate our equation:
plt.annotate("x[0]=.30,R=2.0",(1-.75,x[1]+.03))

#plot:
plt.plot(n,x)

#give it our R and our second x, and do the same as above:
R = 2.0
x = [.31]
for i in range(0,iterations):
    x.append(iterate(x[i],R))
plt.annotate("x[0]=.31,R=2.0",(1,x[1]-.03))
plt.plot(n,x)

#and make that our first graph:
plt.show()

#for the next plot, more iterations are necessary:
iterations = 20
n = list(range(0,iterations+1))
plt.axis([0,len(n)-1,0,1])

#give it our new R and plot two more times with our 2 initial xs:
R = 3.9
x = [.3]
for i in range(0,iterations):
    x.append(iterate(x[i],R))
plt.annotate("x[0]=.30,R=3.9",(15,x[18]))
plt.plot(n,x)

R = 3.9
x = [.31]
for i in range(0,iterations):
    x.append(iterate(x[i],R))
plt.annotate("x[0]=.31,R=3.9",(14,x[17]))
plt.plot(n,x)

#and make that our second graph:
plt.show()
