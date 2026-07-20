class Solution:
    def findMin(self, nums: List[int]) -> int:
        #binary search
        #search space, divide and conquer
        l,r = 0, len(nums) - 1

        while l <r:
            k = l  + (r - l) // 2
            #k = 6, l = 3, r = 2
            #if k and l are in same segment and k > l
            if nums[k] < nums[r]:
                r = k
            else:
                l = k + 1
        return nums[l]


