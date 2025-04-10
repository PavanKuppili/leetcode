class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums=sorted(nums)
        diff=float('inf')
        for i in range(len(nums)-1):
            start=i+1
            end=len(nums)-1
            while(start<end):
                su=nums[i]+nums[start]+nums[end]
                if su==target:
                    return target
                elif abs(target-su)<diff:
                    diff=abs(target-su)
                    ans=su
                elif su>target:
                    end-=1
                else:
                    start+=1
        return ans