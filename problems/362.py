class Object:
    def __init__(self, value):
        self.value = value
        self.count = 1


class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hits = []
        self.total = 0

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        timestamp = Object(timestamp)
        if not self.hits:
            self.total += 1
            self.hits.append(timestamp)

        elif timestamp.value - 299 > self.hits[len(self.hits) - 1].value:
            self.total = 1
            self.hits = [timestamp]
        else:
            while timestamp.value - 299 > self.hits[0].value:
                ts = self.hits.pop(0)
                self.total -= ts.count

            if timestamp.value == self.hits[len(self.hits) - 1].value:
                self.hits[len(self.hits) - 1].count += 1
            else:
                self.hits.append(timestamp)
            self.total += 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        timestamp = Object(timestamp)
        if not self.total:
            return 0

        elif timestamp.value - 299 > self.hits[len(self.hits) - 1].value:
            return 0
        else:
            while timestamp.value - 299 > self.hits[0].value:
                ts = self.hits.pop(0)
                self.total -= ts.count

            return self.total