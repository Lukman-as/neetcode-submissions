class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            search = target - num

            if(search in seen):
                return [seen[search], i]
            seen[num] = i

        return []

        # result = [0, 0]
        # for i in range(len(nums)):
        #     search = target - nums[i]
        #     if(search in nums and i != nums.index(search)):
        #         result[0] = min(i, nums.index(search))
        #         result[1] = max(i, nums.index(search))

        # return result
        