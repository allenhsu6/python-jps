import numpy as np
from scipy.interpolate import UnivariateSpline
import matplotlib.pyplot as plt

def jiecheng(n):
  if n == 0:
      return 1
  if n == 1:
      return 1
  return n * jiecheng(n - 1)

def demo():
    x = np.arange(6)
    y = np.array([3, 1, 4, 1, 5, 9])
    spl = UnivariateSpline(x, y, s=0)
    kn = spl.get_knots()
    for i in range(len(kn)-1):
        cf = [1, 1, 1/2, 1/6] * spl.derivatives(kn[i])
        print("For {0} <= x <= {1}, p(x) = {5}*(x-{0})^3 + {4}*(x-{0})^2 + {3}*(x-{0}) + {2}".format(kn[i], kn[i+1], *cf))
        dx = np.linspace(kn[i], kn[i+1], 100)
        dy = []
        for item in dx:
            dy.append(pow((item-kn[i]),3)*cf[3]+pow((item-kn[i]),2)*cf[2]+(item-kn[i])*cf[1]+cf[0])
        plt.plot(dx, dy, "-r")
        plt.plot(x, y, "og")
        plt.plot(x, y, "-b")



def my_curve_fit():
    path = [[5, 117], [12, 110], [12, 105], [13, 104], [15, 102], [20, 97], [22, 95], [22, 73], [24, 71], [29, 66], [30, 66], [31, 65], [32, 64], [37, 59], [41, 55], [41, 54], [42, 53], [44, 51], [44, 35], [45, 34], [50, 29], [57, 29], [58, 28], [63, 23], [70, 16], [84, 16], [85, 15]]

    points = np.array(path)
    x = points[:,0]
    x = [float(a) for a in x]
    b = set()
    for i in range(len(x)):
        if x[i] in b:
            x[i] = x[i] + 0.1
        else:
            b.add(x[i])
    y = points[:,1]
    plt.plot(x, y, "og")
    spl = UnivariateSpline(x, points[:,1], s=0)
    kn = spl.get_knots()
    lst = []
    for i in range(4):
        lst.append(1/jiecheng(i))
    for i in range(len(kn)-1):
        cf = lst * spl.derivatives(kn[i])
        print("For {0} <= x <= {1}, p(x) = {5}*(x-{0})^3 + {4}*(x-{0})^2 + {3}*(x-{0}) + {2}".format(kn[i], kn[i+1], *cf))
        dx = np.linspace(kn[i], kn[i+1], 10)
        dy = []
        for item in dx:
            dy.append(pow((item-kn[i]),3)*cf[3]+pow((item-kn[i]),2)*cf[2]+(item-kn[i])*cf[1]+cf[0])
        plt.plot(dx, dy, "-r")

if __name__ == '__main__':
    plt.figure()
    plt.grid(True)
    demo()
    plt.show()
