class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxProd = 0
        # for i in range(len(heights)):
        #     left = i
        #     right = len(heights) - 1

        #     while left<right:
        #         prod = min(heights[right],heights[left])*(right - left)
        #         maxProd = max(maxProd, prod)
        #         right -= 1
        left = 0
        right = len(heights) - 1
        while left < right:

            prod = min(heights[right],heights[left])*(right - left)
            maxProd = max(maxProd, prod)
            if heights[left] < heights[right]:
                left+=1
            else:
                right -= 1


        return maxProd

        