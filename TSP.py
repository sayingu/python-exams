import random
import math
import matplotlib as mpl
import matplotlib.pyplot as plt


class TSP:
    # nodes = [[random.randrange(0, 100), random.randrange(0, 100)]
    #          for i in range(20)]
    nodes = [[0, 1], [13, 20], [20, 85], [30, 1], [39, 70], [99, 75], [9, 17], [92, 74], [29, 10], [5, 20], [
        34, 99], [52, 83], [90, 87], [64, 34], [23, 85], [46, 79], [33, 81], [44, 22], [33, 66], [21, 76]]

    path = []

    # Random Algorithm
    def make_random_path(self):
        result = self.nodes

        random.shuffle(result)

        if len(result) > 0:
            result.append(result[0])

        # update with the new path
        self.set_new_path(result, 'Random Algorithm')

    # Greedy Algorithm
    def make_greedy_path(self):
        # make a pool containing all nodes
        # pool = list(range(len(self.nodes)))
        pool = self.nodes
        result = []

        # pop the first node from the pool and append to the result
        result.append(pool.pop(0))

        # while there are any remaining node
        while len(pool) > 0:
            # initialize min_dist and min_index
            min_dist = None
            min_index = None

            # for every remaining nodes
            for i in range(len(pool)):
                # get the most recently added node
                node1 = result[len(result) - 1]
                # the current remaining node
                node2 = pool[i]
                # calculate the distance between two ( using self.calc_dist() )
                dist = self.calc_dist(node1, node2)
                if min_dist is None or dist < min_dist:
                    min_dist = dist
                    min_index = i

            result.append(pool.pop(min_index))

        result.append(result[0])

        self.set_new_path(result, 'Greedy Algorithm')

    def calc_dist(self, node1, node2):
        return math.sqrt((node2[0] - node1[0]) ** 2 + (node2[1] - node1[1]) ** 2)

    # 2-Opt Algorithm
    def make_2opt_path(self):
        # make a path
        self.make_random_path()

        result = self.path

        # loop 100 times
        for i in range(100000):
            # modify the current path
            # select random two node indices
            j = random.randint(1, len(result)-2)
            k = random.randint(j, len(result)-2)

            # slice the path with three segments (path1, path2, path3)
            path1 = result[:j]
            path2 = result[j:k]
            path3 = result[k:]
            path2.reverse()
            new_path = path1 + path2 + path3
            pathLenth = self.calc_path_length(result)
            if pathLenth > self.calc_path_length(new_path):
                result = new_path
                pathLenth = self.calc_path_length(new_path)

            # self.draw(result, str(i) + ': ' + str(pathLenth), True)

        self.set_new_path(result, '2-Opt Algorithm')

    def calc_path_length(self, path):
        dist = 0.0
        for i in range(len(path) - 1):
            dist += math.sqrt((path[i + 1][0] - path[i][0])
                              ** 2 + (path[i + 1][1] - path[i][1]) ** 2)
        return dist

    def set_new_path(self, result, algorithmName):
        self.path = result
        print('path:', self.path)
        print('algorithmName:', algorithmName)
        distance = math.floor(self.calc_path_length(self.path))
        print('distance:', distance)
        self.draw(self.path, algorithmName + ': ' + str(distance), False)

    def draw(self, result, title, clear):
        plt.title(title)
        plt.scatter([p[0] for p in self.nodes], [p[1] for p in self.nodes])
        plt.plot([p[0] for p in result], [p[1] for p in result])
        plt.draw()
        plt.pause(.1)
        if clear:
            plt.clf()


tsp = TSP()
plt.ion()
tsp.make_2opt_path()
plt.ioff()
with mpl.rc_context(rc={'interactive': False}):
    plt.show()
