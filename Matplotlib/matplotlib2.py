# Most of the Matplotlib utilities lies under the pyplot submodule

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0,8])
ypoints = np.array([0, 200])

plt.plot(xpoints, ypoints)
plt.show()

# The plot() function is used to draw points (markers) in a diagram.
# By default, the plot() function draws a line from point to point.
# The function takes parameters for specifying points in the diagram.
# Parameter 1 is an array containing the points on the x-axis.
# Parameter 2 is an array containing the points on the y-axis.
# If we need to plot a line from (1, 3) to (8, 10), we have to pass two arrays [1, 8] and [3, 10] to the plot function.

xp = np.array([1, 8])
yp = np.array([3, 10])
plt.plot(xp, yp)
plt.show()

# Plotting Without Line
# To plot only the markers, you can use shortcut string notation parameter 'o', which means 'rings'.
# plt.plot(xp, yp, 'o')
# plt.show()


# Multiple Points
# Draw a line in a diagram from position (1, 3) to (2, 8) then to (6, 1) and finally to position (8, 10):

xp1 = np.array([1,2,6,8])
yp1 = np.array([3, 8, 1, 10])
plt.plot(xp1, yp1)
plt.show()


# Default X-Points
# If we do not specify the points in the x-axis, they will get the default values 0, 1, 2, 3, (etc. depending on the length of the y-points.

yp2 = np.array([3, 8, 1, 10, 5, 7])
# plt.plot(yp2)
plt.plot(yp2, marker = 'o')
plt.show()

# Multiple Lines
# You can plot as many lines as you like by simply adding more plt.plot() functions:
y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])
plt.plot(y1)
plt.plot(y2)
plt.show()

# x1 = np.array([0, 1, 2, 3])
# y1 = np.array([3, 8, 1, 10])
# x2 = np.array([0, 1, 2, 3])
# y2 = np.array([6, 2, 7, 11])
# plt.plot(x1, y1, x2, y2)
# plt.show()