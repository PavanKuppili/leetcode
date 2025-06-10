class Solution:
    def maxDifference(self, s: str) -> int:
        c=Counter(s)
        odd=0
        even=len(s)
        for count in c.values():
            if count%2==1:
                odd=max(odd,count)
            elif count!=0:
                even=min(even,count)
        return odd-even