class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_num=""
        for i in range(len(num)-2):
            if num[i]==num[i+1]==num[i+2]:
                trip=num[i:i+3]
                max_num= max(trip,max_num)
        return max_num