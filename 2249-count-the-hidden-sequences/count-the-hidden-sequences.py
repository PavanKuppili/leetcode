class Solution:
    def numberOfArrays(self, diff: List[int], lower: int, upper: int) -> int:
        a = maxima = minima = 0
        for d in range(len(diff)):
            a += diff[d]
            maxima = max(maxima, a)
            minima = min(minima, a)
        return max(0, (upper - lower) - (maxima - minima) + 1)