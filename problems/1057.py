# Time O(N^2*M^2), almost suboptimal

'''
class WorkerToByke:
    def __init__(self, worker, bike, distance):
        self.worker = worker
        self.bike = bike
        self.distance = distance

    def __repr__(self):
        return f'worker:{self.worker}, bike:{self.bike}, distance:{self.distance}'


class Solution:
    def assignBikes(self, workers, bikes):
        distances = []
        for i, worker in enumerate(workers):
            for j, bike in enumerate(bikes):
                distances.append(WorkerToByke(i, j, abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])))

        distances.sort(key=lambda s: s.distance)
        used_bikes = [None for _ in range(len(bikes))]
        assigned_workers = [None for _ in range(len(workers))]
        worker_to_bike = [None for _ in range(len(workers))]
        i = 0
        assigned_worker_num = 0
        while assigned_worker_num != len(workers):
            j = i
            while j < len(distances) and distances[j] == distances[i]:
                j += 1

            if j == i + 1 and (used_bikes[distances[i].bike] is None) and assigned_workers[distances[i].worker] is None:
                worker_to_bike[distances[i].worker] = distances[i].bike
                used_bikes[distances[i].bike] = 1
                assigned_workers[distances[i].worker] = 1
                assigned_worker_num += 1
                i += 1
            else:

                worker_to_bike_with_min_index = None
                for k in range(i, j):
                    if (used_bikes[distances[k].bike] is None) and (assigned_workers[distances[k].worker] is None) and (
                            worker_to_bike_with_min_index is None or (distances[k].worker < worker_to_bike_with_min_index.worker and distances[k].bike < worker_to_bike_with_min_index.bike)):
                        worker_to_bike_with_min_index = distances[k]

                if worker_to_bike_with_min_index:
                    worker_to_bike[worker_to_bike_with_min_index.worker] = worker_to_bike_with_min_index.bike
                    used_bikes[worker_to_bike_with_min_index.bike] = 1
                    assigned_workers[worker_to_bike_with_min_index.worker] = 1
                    assigned_worker_num += 1
                    i += 1
                else:
                    i = j

        return worker_to_bike
'''


class Solution:
    def assignBikes(self, workers, bikes):
        distances = [[] for _ in range(2001)]
        for i, worker in enumerate(workers):
            for j, bike in enumerate(bikes):
                dis = abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])
                distances[dis].append((i, j))

        worker_to_bike, used_bikes = [-1 for _ in range(len(workers))], set()

        for d in range(len(distances)):
            for i, j in distances[d]:
                if worker_to_bike[i] == -1 and j not in used_bikes:
                    worker_to_bike[i] = j
                    used_bikes.add(j)

        return worker_to_bike


s = Solution()
print(s.assignBikes([[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0]], [[0,999],[1,999],[2,999],[3,999],[4,999],[5,999],[6,999],[7,999],[8,999]]
))