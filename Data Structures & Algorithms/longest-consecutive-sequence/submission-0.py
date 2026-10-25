class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        left = 0
        right = 1
        maxLen = 1
        dups = 0

        while right < len(nums):
            if nums[right] == nums[right - 1]:
                dups += 1
                right += 1
                continue
            if nums[right] - nums[right - 1] == 1:
                right += 1
            else:
                maxLen = max(maxLen, right - left - dups)
                left = right
                right += 1
                dups = 0
        maxLen = max(maxLen, right - left - dups)
        return maxLen
                



            
        