# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 20:17:17 2018

@author: Stefan
"""

import matplotlib.pyplot as pl
import numpy as np

filePath = "kalibration.txt"

points = np.loadtxt(filePath).transpose()
print(points[1])

# if necessary, log-transform all y values 
#points[2, :] = np.log10(points[2, :])
#points[:,1:] = np.log10(points[:,1:])
#points = points[:,1:]
# store current best fits & minimal errors

bestErrorsL = np.inf
bestLineEqL = np.nan

bestErrorsR = np.inf
bestLineEqR = np.nan

numpnts = points.shape[1]
assert numpnts >= 6, "Not enough data points available for proper fits."

# iterate over the data set, splitting it at a moving pivot point n
# fit linear functions to z´the left (L) and right (R) point sets
# if a better fit combination than the one currently stored is found,
# update the corresponding optimum fit & error variables   
for n in range(3, numpnts-2):
    print("splitting at n =", n, "...")
    # split point data into two sets (L & R)
    pointsL = points[:, 0:n] 
    pointsR = points[:, n:numpnts]
    #print(pointsL, pointsR)
    # find fit coefficients for a first degree polynomial (a line)
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!change here
    resultL = np.polyfit(pointsL[0, :], pointsL[4, :], 1, full = True)
    coeffsL = resultL[0]
    errorsL = resultL[1][0]
    #!!!!!!!!!!!!!!!!!!!!!and here
    resultR = np.polyfit(pointsR[0, :], pointsR[4, :], 1, full = True)
    coeffsR = resultR[0]
    errorsR = resultR[1][0]    
    # create a polynomial function object from coefficients "c"
    lineEqL = np.poly1d(coeffsL)
    lineEqR = np.poly1d(coeffsR)
    # output the polynomial equation to the console
    print("L fit: f(x) = ", lineEqL, ", error =", errorsL)
    print("R fit: f(x) = ", lineEqR, ", error =", errorsR)
    # if summed error < stored error, update the best fits
    if (errorsL + errorsR) < (bestErrorsL + bestErrorsR):
       bestErrorsL = errorsL
       bestErrorsR = errorsR
       bestLineEqL = lineEqL
       bestLineEqR = lineEqR
       print("best fits have been updated!")


# compute x intersection point of the two optimal fits
x0 = np.roots(bestLineEqL - bestLineEqR)[0]


print("final best fits:")
print("L fit: f(x) = ", lineEqL, ", error =", errorsL)
print("R fit: f(x) = ", lineEqR, ", error =", errorsR)

print("intersection at x0 =", x0)

pl.plot(points[0, :], points[1, :], "o-", points[0, :], bestLineEqL(points[0, :]), "-", points[0, :], bestLineEqR(points[0, :]), "-")
