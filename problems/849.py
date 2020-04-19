class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        memo = [None] * len(seats)
        closest_person = float("+inf")
        for i in range(len(seats)):
            if seats[i] == 1:
                closest_person = 0

            memo[i] = closest_person
            closest_person += 1

        closest_person = float("+inf")
        for i in range(len(seats) - 1, -1, -1):
            if seats[i] == 1:
                closest_person = 0

            memo[i] = min(closest_person, memo[i])
            closest_person += 1

        return max(memo)