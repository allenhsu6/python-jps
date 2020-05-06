import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
from curve import process_by_same_x, process_by_distance
path = [[1, 3], [3, 5], [3, 16], [4, 17], [6, 15], [6, 5], [7, 4], [9, 6], [9, 16], [10, 17], [12, 15], [12, 5], [13, 4], [15, 6], [15, 16], [16, 17], [18, 15], [18, 5], [19, 4], [21, 6], [21, 19]]
points = process_by_same_x(np.array(path))
process_by_same_x(points, 4)
# points = np.array(path)
print(np.shape(points))
x = points[:, 0]
y = points[:, 1]

x = [float(a) for a in x]
b = set()
delete_list = []
for i in range(len(x)):
    if x[i] in b:
        delete_list.append(i)
    else:
        b.add(x[i])
points = np.delete(points,delete_list,axis=0)

print(np.shape(points))
x = points[:, 0]
y = points[:, 1]
plt.plot(x, y, 'ro', ms=2)

spl = UnivariateSpline(x, y)
xs = np.linspace(-3, 3, 1000)
plt.plot(xs, spl(xs), 'g', lw=3)


spl.set_smoothing_factor(0.8)
plt.plot(xs, spl(xs), 'b', lw=3)
plt.show()