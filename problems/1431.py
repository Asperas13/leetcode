class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        answer = []

        for cd in candies:
            answer.append(cd + extraCandies >= max_candies)

        return answer
