class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        res = 0
        curr_k = 0
        cnt = defaultdict(int)
        l = 0
        for r in range(len(nums)):
            curr_k += cnt[nums[r]]
            cnt[nums[r]] += 1
            while k <= curr_k:
                cnt[nums[l]] -= 1 
                curr_k -= cnt[nums[l]]
                l += 1
            res += l 

        return res