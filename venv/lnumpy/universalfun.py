#arithmetic, trigonometric, statistics
import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as pylt

x = [1,2,3,4,5]
y = [2,4,6,7,10]

pylt.plot(x,y,marker='x')
pylt.grid(True)
pylt.xlabel("x-axis")
pylt.ylabel("y-axis")
pylt.title("sim")
pylt.show()