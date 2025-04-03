# O(n)
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res, i_mx, d_mx = 0, 0, 0
        for x in nums:
            # maximize res
            res = max(res, d_mx * x) # x as nums[k]
            # maximize (nums[i] - nums[j])
            d_mx = max(d_mx, i_mx - x) # x as nums[j]
            # maximize nums[i]
            i_mx = max(i_mx, x) # x as nums[i]
        return res