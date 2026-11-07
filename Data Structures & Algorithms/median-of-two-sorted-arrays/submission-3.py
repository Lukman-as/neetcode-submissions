class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i,j = 0, 0
        new = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                new.append(nums1[i])
                i += 1
            else:
                new.append(nums2[j])
                j += 1
                
        new.extend(nums1[i:])
        new.extend(nums2[j:])
        print(new)
        if len(new)%2 == 0:
            return (float)(new[len(new)//2 - 1] + new[len(new)//2])/2
        else:
            return (float)(new[len(new)//2])

        
            




        