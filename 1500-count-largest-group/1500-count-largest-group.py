from collections import defaultdict

class Solution:
    def countLargestGroup(self, n: int) -> int:
        def digit_sum(x: int) -> int:
            return sum(int(d) for d in str(x))
        
        groups = defaultdict(int)
        
        for i in range(1, n + 1):
            s = digit_sum(i)
            groups[s] += 1
        
        max_size = max(groups.values())
        return sum(1 for count in groups.values() if count == max_size)