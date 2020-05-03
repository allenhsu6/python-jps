import csv
import matplotlib.pyplot as plt
from plot import MapInfo

obstacle = []
m = MapInfo()

class Instance:
    def __init__(self, matrix, matrixWidth, matrixHeight, startX, startY, endX, endY):
        self.matrix = matrix
        self.matrixWidth = matrixWidth
        self.matrixHeight = matrixHeight
        self.startX = startX
        self.startY = startY
        self.endX = endX
        self.endY = endY

class InstanceUtilities:
    @staticmethod
    def readCSVInstance(url):
        matrix = []

        with open(url) as csv_file:
            csvReader = csv.reader(csv_file, delimiter=';')
            startX = None
            startY = None
            endX = None
            endY = None

            colCount = 0 # x max
            rowCount = 0 # y max

            rowIdx = 0
            colIdx = 0

            for row in csvReader:
                matrix.append([])

                colIdx = 0
                for col in row:

                    if col == 'X':
                        matrix[rowIdx].append(False)
                        obstacle.append((colIdx, rowIdx))

                    else:
                        if col == 'S':
                            startX = colIdx
                            startY = rowIdx
                            m.start = (startX, startY)
                        elif col == 'E':
                            endX = colIdx
                            endY = rowIdx
                            m.end = (endX, endY)
                        matrix[rowIdx].append(True)
                    colIdx = colIdx + 1
                
                if 0 < colCount != colIdx:
                    raise Exception("The instance must have a constant columns count.")
                else:
                    colCount = colIdx
                
                rowIdx = rowIdx + 1
            rowCount = rowIdx
            # todo: 这里图像的长宽外围，可以自己设置
            m.height = rowCount
            m.width = colCount

        m.obstacle = obstacle
        m.show()
        if (startX == None):
            raise Exception("The instance must have a start node.")
        
        if (endX == None):
            raise Exception("The instance must have a end node.")

        return Instance(matrix, colCount, rowCount, startX, startY, endX, endY)

    @staticmethod
    def displayInstanceWithPath(instance, path):
        print(len(path))
        for node in path:
            while path.count(node) > 1:
                path.remove(node)
        m.path = path
        plt.show()
        print(len(path))




