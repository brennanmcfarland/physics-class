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

#give it our R and our first x, the first y is calculated:
R = 3.55
x = [.0001]

y = [iterate(x[0],R)]

#for 100 iterations, find the next x and y by iterating:
#note that the loop goes 200 times because it is calculating 2 ys for each x
for i in range(0,201):
    y.append(iterate(x[i],R))
    x.append(y[i])

#now get rid of all the xs and ys except for the last, the  hundredth iteration:
x = [x[len(x)-1]]
y = [x[0]]

#and iterate out another 20 iterations to see the periodicity:
#notice: it is a period 8 attractor!
for i in range(0,40):
    y.append(iterate(x[i],R))
    x.append(y[i])

#format the axes, plot the curve and y=x line, this part is not important, just visually helpful
plt.axis([0,1,0,1])
plt.plot([0,1])
curvepoints = graphfunction(0,1,.01,iterate,R)
plt.plot(curvepoints[0],curvepoints[1])

#print out our set of x values, our set of n steps:
print("The next 20 steps after n=100 are: ")
for i in range(0,int(len(x)/2)):
    print(x[i*2+1])
print("It is a period 8 attractor. ")

#and plot our logistic difference equation
plt.plot(x,y)
plt.show()
