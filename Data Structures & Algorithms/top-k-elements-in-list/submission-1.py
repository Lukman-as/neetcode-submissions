class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1

        d = sorted(count, key=count.get)
        result = []
        for i in range(len(d) - 1, len(d) - k - 1, -1):
            result.append(d[i])
        return result
        
        
        