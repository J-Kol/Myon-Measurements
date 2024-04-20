import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit 

points = np.loadtxt("Lifetime measurement.txt")
X = points[:,0]
Y = points[:,1]

#xdata = np.asarray(X) 
#ydata = np.asarray(Y) 

def func(x, a, t):
    return a*np.exp(-x*t)

estimates = [58, 2]
popt, _ = curve_fit(func, X, Y, p0 = estimates)
# summarize the parameter values
a, t = popt
#func(popt)
plt.plot(X, Y, "+", linewidth = 4, color=(0, 0, 0),label="Function Value")
#plt.ylim(-10,10)

X_test = np.linspace(0, 8.5)
plt.plot(X_test, func(X_test, *popt), "-", linewidth = 4, color=(1, 0, 0),label="Function Value")
#plt.ylim(-10,10)
plt.grid()
plt.xlabel("time")
plt.ylabel("events")
plt.title("Graph",fontsize = 18);
#print(popt)
#HWZ = t/np.log(2)
#print(t, HWZ)
plt.show()
