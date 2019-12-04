import random
import math


class TSP:
    nodes = [[random.randrange(0, 50), random.randrange(0, 20)]
             for i in range(4)]

    # Random Algorithm
    def make_random_path(self):
        result = list(range(4))

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

        # loop 100 times
        for i in range(100):
            # modify the current path
            # select random two node indices
            i = 0 # EDIT THIS
            k = 0 # EDIT THIS

# i = random.randint(1, len(path)-2) # Edit this
# k = random.randint(i, len(path)-2) # Edit this
# print(i, k)

            # slice the path with three segments (path1, path2, path3)
            path1 = [] # EDIT THIS
            path2 = [] # EDIT THIS
            path3 = [] # EDIT THIS

# path1 = path[:i]
# path2 = path[i:k]
# path3 = path[k:]
# path2.reverse()
# path = path1 + path2 + path3

    def set_new_path(self, result, algorithmName):
        print('result:', result)
        print('algorithmName:', algorithmName)


tsp = TSP()
tsp.make_random_path()
tsp.make_greedy_path()
