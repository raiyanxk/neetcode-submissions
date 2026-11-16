class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0
        r = len(nums) - 1
        res = float('inf')

        while l <= r:
            mid = (l + r) // 2

            # if we are in the sorted part of the array
            if nums[l] < nums[r]:
                return min(res, nums[l])
            
            # 
            if nums[mid] > nums[r]:
                res = min(res, nums[r])
                l = mid + 1
            else:
                res = min(res, nums[mid])
                r = mid - 1

        return res