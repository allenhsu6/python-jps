import sys
import time
sys.path.append('src')

from src.pathplanning import PathPlanning
from src.grid import Grid
from src.instance import InstanceUtilities

from src.colors import Colors

def executeJPSOnCSVInstance(url):
    print('Reading the instance..')

    instance = InstanceUtilities.readCSVInstance(url)

    print('Done.')

    grid = Grid(instance.matrixWidth, instance.matrixHeight, instance.matrix)
    grid.buildNodes()

    print('Computing JPS..')

    startTime = time.time()

    method = PathPlanning(grid)
    path = method.findPath(instance.startX, instance.startY, instance.endX, instance.endY, 'A*')

    endTime = time.time() - startTime

    InstanceUtilities.displayInstanceWithPath(path)

    Colors.queryPrintColor(Colors.GREY)

    print('Done. Result computed in ' + str(endTime) + ' ms.')
    print("Expand node number is: " + str(method.expendCount) + '.')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        executeJPSOnCSVInstance(sys.argv[1])
    else:
        print('Please pass a valid instance CSV file as first argument.')