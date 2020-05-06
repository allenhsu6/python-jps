import sys
import time
sys.path.append('src')

from src.pathplanning import PathPlanning
from src.grid import Grid
from src.instance import InstanceUtilities
from src.curve import curve_show
from utils import pathLength,rmRepeatedPoint
def executeJPSOnCSVInstance(url):
    instance = InstanceUtilities.readCSVInstance(url)

    grid = Grid(instance.matrixWidth, instance.matrixHeight, instance.matrix)
    grid.buildNodes()

    print('Computing ...')

    startTime = time.time()

    method = PathPlanning(grid)
    use_method = 'w_jps' # 这里可以选择jps 或者 A* 或者w_jps
    path = method.findPath(instance.startX, instance.startY, instance.endX, instance.endY, use_method)
    endTime = time.time() - startTime
    rmRepeatedPoint(path)
    InstanceUtilities.displayInstanceWithPath(path)
    curve_show(path)
    print('Done. '+ use_method +' Result computed in ' + str(endTime) + ' ms.')
    print("Expand node number is: " + str(method.expendCount) + '.')
    print("path length is: " + str(pathLength(path)))
if __name__ == '__main__':

    if len(sys.argv) > 1:
        executeJPSOnCSVInstance(sys.argv[1])
    else:
        print('Please pass a valid instance CSV file as first argument.')