import matplotlib.pyplot as plt
import numpy as np

filepath = "kalibration.txt"

points = np.loadtxt(filepath)#.transpose()
#points[:,1:] = np.log10(points[:,1:])
#points = points[2:]
# delete 1 frm channel0 2
#points[:,2] = np.log10(points[:,2])

#print(points)

brechpunkt = int(input("Enter the threshold to be tested: "))

#print(points)

class graph():

    def __init__(self, x, chan, line, c):
        self.x = x
        self.chan = chan
        self.line = line
        self.c = c
    
    def zeichnen(self):
        plt.plot(self.x, self.chan, \
        self.line, linewidth = 4, color=self.c,label="Function Value")

all_x = [] #alle x-werte
all_xb = [] #die x-werte vor dem Brechpunkt chan0
y_chan0 = [] #alle y-werte für chan0
y_chan0b = [] #die y-werte mit Brechpunkt chan0
y_chan1 = [] #alle y-werte für chan1
y_chan1b = [] #die y-werte mit Brechpunkt chan1
y_chan2 = [] #alle y-werte für chan2
y_chan2b = [] #die x-werte mit Brechpunkt chan2
y_chan3 = [] #alle y-werte für chan2
y_chan3b = [] #die x-werte mit Brechpunkt chan2

zeichnen = graph(all_x, y_chan0, "-", (0.0,1,0.6))
zeichnenb = graph(all_xb, y_chan0b, "--", (0.0,1,0.6))
zeichnen1 = graph(all_x, y_chan1, "-", (0.0,0,0.8))
zeichnen1b = graph(all_xb, y_chan1b, "--", (0.0,0,0.8))
zeichnen2 = graph(all_x, y_chan2, "-", (0.5,0,0.6))
zeichnen2b = graph(all_xb, y_chan2b, "--", (0.5,0,0.6))
zeichnen3 = graph(all_x, y_chan3, "-", (0.5,0,0.6))
zeichnen3b = graph(all_xb, y_chan3b, "--", (0.5,0,0.6))

i = 0
for n in points:
    #print(points[i][0])
    all_x.append(points[i][0])
    y_chan0.append(points[i][1])
    y_chan1.append(points[i][2])
    y_chan2.append(points[i][3])
    y_chan3.append(points[i][4])
    i += 1

all_xb.append(all_x[0])
all_xb.append(brechpunkt)

all_xb.append(brechpunkt)
all_xb.append(all_x[-1])

i = 0
for p in all_x:
    while not all_x[i] == brechpunkt:
        i += 1

#print(y_chan0[i])
y_chan0b.append(y_chan0[0])
y_chan0b.append(y_chan0[i])

y_chan0b.append(y_chan0[i])
y_chan0b.append(y_chan0[-1])

y_chan1b.append(y_chan1[0])
y_chan1b.append(y_chan1[i])

y_chan1b.append(y_chan1[i])
y_chan1b.append(y_chan1[-1])

y_chan2b.append(y_chan2[0])
y_chan2b.append(y_chan2[i])

y_chan2b.append(y_chan2[i])
y_chan2b.append(y_chan2[-1])

y_chan3b.append(y_chan3[0])
y_chan3b.append(y_chan3[i])

y_chan3b.append(y_chan3[i])
y_chan3b.append(y_chan3[-1])

difference = sum(abs(y1 - y2) for y1, y2 in zip(y_chan0, y_chan0b))
difference1 = sum(abs(y1 - y2) for y1, y2 in zip(y_chan1, y_chan1b))
difference2 = sum(abs(y1 - y2) for y1, y2 in zip(y_chan2, y_chan2b))
difference3 = sum(abs(y1 - y2) for y1, y2 in zip(y_chan2, y_chan3b))
#difference_all = difference + difference1 + difference2
#print(f"Der Unterschied zwischen den Graphen zeichnen() und zeichnenb() ist {difference}, der Unterschied zwischen den Graphen zeichnen1() und zeichnenb1() ist {difference1} zwischen den Graphen zeichnen2() und zeichnen2b() ist der Unterschied {difference2} und der Unterschied zwischen den Graphen zeichnen3() und zeichnen3b() ist {difference3}")
print(difference, difference1, difference2, difference3)

zeichnen.zeichnen()
zeichnen1.zeichnen()
zeichnen2.zeichnen()
zeichnen3.zeichnen()

#plt.ylim(-10,10)
plt.grid()
plt.xlabel("mV")
plt.ylabel("ch")
plt.title("Kalibration",fontsize = 18);
plt.show()

zeichnen.zeichnen()
zeichnenb.zeichnen()
plt.show()

zeichnen1.zeichnen()
zeichnen1b.zeichnen()
plt.show()

zeichnen2.zeichnen()
zeichnen2b.zeichnen()
plt.show()

zeichnen3.zeichnen()
zeichnen3b.zeichnen()
plt.show()
