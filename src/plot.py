# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import copy


class MapInfo(object):
    def __init__(self):
        self.width = 0
        self.height = 0

        self._start = (-1, -1)
        self._end = (-1, -1)
        self._obstacle = []
        self._open = (-1, -1)
        self._close = (-1, -1)
        self._path = []
        self._roadmap = dict()
        plt.figure()

    @staticmethod
    def draw_point(p, shape, color):
        plt.plot(p[0], p[1], shape, color=color)

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, s):
        self._start = s
        self.draw_point(self._start, 'o', color='green')

    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, e):
        self._end = e
        self.draw_point(self._end, 'o', color='red')

    @property
    def obstacle(self):
        return self._obstacle

    @obstacle.setter
    def obstacle(self, o):
        self._obstacle = copy.deepcopy(o)
        t = list(zip(*self.obstacle))
        plt.plot(t[0], t[1], 's', color='black')


    @property
    def roadmap(self):
        return self._roadmap

    @roadmap.setter
    def roadmap(self, o):
        self._roadmap = copy.deepcopy(o)
        t = zip(*self.roadmap.keys())
        plt.plot(t[0], t[1], '.', color='blue')
        for k, v in self.roadmap.items():
            for p in v:
                plt.plot([k[0], p[0]], [k[1], p[1]], color='lightblue')

    @property
    def open(self):
        return self._open

    @open.setter
    def open(self, o):
        self._open = o
        plt.plot(self.open[0], self.open[1], 'x', color='green')


    @property
    def close(self):
        return self._close

    @close.setter
    def close(self, o):
        self._close = o
        plt.plot(self.close[0], self.close[1], 'x', color='blue')


    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, o):
        self._path = copy.deepcopy(o)
        t = list(zip(*self.path))
        plt.plot(t[0], t[1], color='purple')

    def show(self):
        plt.axis('equal')
        _border_x = [0, self.width, self.width, 0, 0]
        _border_y = [0, 0, self.height, self.height, 0]
        plt.plot(_border_x, _border_y, 'black')
        plt.grid(True)

if __name__ == "__main__":
    m = MapInfo()
    m.show()    # 画墙
    m.start = (10, 10)
    m.end = (50, 30)
    m.obstacle = [(20, i) for i in range(30)]
    m.path = [(10, i) for i in range(30)]
    plt.show()
