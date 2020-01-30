from collections import defaultdict


class StoredValue:
    def __init__(self, value, timestamp):
        self.value = value
        self.timestamp = timestamp

    def update(self, value, timestamp):
        self.value = value
        self.timestamp = timestamp


class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.storage = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        stored_value = StoredValue(value, timestamp)
        if key not in self.storage:
            self.storage[key].append(stored_value)
        else:
            index = self._binary_search(self.storage[key], timestamp)
            if self.storage[key][index].value == value:
                self.storage[key][index].update(value, timestamp)
            else:
                self.storage[key].append(stored_value)

    def get(self, key: str, timestamp: int) -> str:
        if key in self.storage:
            index = self._binary_search(self.storage[key], timestamp)
            stored_value = self.storage[key][index]
            if stored_value.timestamp <= timestamp:
                return self.storage[key][index].value
        return ''

    def _binary_search(self, search_list, timestamp):
        lo, hi = 0, len(search_list) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if search_list[mid].timestamp == timestamp:
                return mid
            elif search_list[mid].timestamp > timestamp:
                hi = mid - 1
            else:
                lo = mid + 1

        return lo - 1

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)