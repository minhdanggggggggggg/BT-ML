import math
import numpy as np 
import matplotlib.pyplot as plt

def grad(x):
    return 6*x + 2 + 4*np.cos(x)
def cost(x):
    return 3*(x**2) + 2*x + 4*np.sin(x)
#grad =  6*x+ 4*np.cos(x)+2
#cost =  3*x**2 + 2*x +  4*np.sin(x)
def myGD1(eta, x0):
    x = [x0]
    for it in range(100):
        x_new = x[-1] - eta*grad(x[-1])
        if abs(grad(x_new)) < 1e-3:
            break
        x.append(x_new)
    return (x, it)
(x1, it1) = myGD1(.01, -1) #x0 = -1
(x2, it2) = myGD1(.1, 5) #x0 = 5
print('x1 = %f, cost = %f, after %d'%(x1[-1], cost(x1[-1]), it1))
print('x2 = %f, cost = %f, after %d'%(x2[-1], cost(x2[-1]), it2))

