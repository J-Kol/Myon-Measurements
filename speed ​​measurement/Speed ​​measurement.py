import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit 

points = np.loadtxt("Speed ​​measurement.txt")
X = points[:,0]
Y = points[:,1]

#xdata = np.asarray(X) 
#ydata = np.asarray(Y) 

def func(x, mu, sig, a):
    return a*np.exp(-np.power((x - mu)/sig, 2.)/2)

estimates = [10, 2, 23]
popt, _ = curve_fit(func, X, Y, p0 = estimates)
# summarize the parameter values
mu, sig, a = popt
#func(popt)
plt.plot(X, Y, "+", linewidth = 4, color=(0, 0, 0),label="Function Value")
#plt.ylim(-10,10)

X_test = np.linspace(0, 25, 100)
plt.plot(X_test, func(X_test, *popt), "-", linewidth = 4, color=(1, 0, 0),label="Function Value")
#plt.ylim(-10,10)
plt.grid()
plt.xlabel("speed")
plt.ylabel("events")
plt.title("Speed test",fontsize = 18);
print(popt)
seconds = mu*10**(-9)
height = 3.2
v = height/seconds
c = 3*10**(8)
print(f"The average speed of our muons is {v} and {v/c} times the speed of light.")
plt.show()
