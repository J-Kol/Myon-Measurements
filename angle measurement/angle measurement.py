import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit 

points = np.loadtxt("angle measurement.txt")
X = points[:,0]
Y = points[:,1]

#xdata = np.asarray(X) 
#ydata = np.asarray(Y) 

def func(x, n, a, t):
    return a* np.cos(np.deg2rad(90-x)) ** n + t

estimates = [0.112, 1, 0.006]
popt, _ = curve_fit(func, X, Y, p0 = estimates)
# summarize the parameter values
n, a, t = popt
#func(popt)
plt.plot(X, Y, "+", linewidth = 4, color=(0, 0, 0),label="Function Value")
#plt.ylim(-10,10)

X_test = np.linspace(0, 90)
plt.plot(X_test, func(X_test, *popt), "-", linewidth = 4, color=(1, 0, 0),label="Function Value")
#plt.ylim(-10,10)
plt.grid()
plt.xlabel("degree")
plt.ylabel("events")
plt.title("Graph",fontsize = 18);
print(popt)
plt.show()
