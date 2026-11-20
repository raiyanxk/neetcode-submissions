class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:


        def qselect(nums, k):

            pivot = nums[0]
            small = []
            eq = 0
            big = []

            # need to find all nums < pivot
            for num in nums:
                if num < pivot:
                    small.append(num)
                elif num > pivot:
                    big.append(num)
                else:
                    eq += 1

            if k < len(big):
                return qselect(big, k)
            elif k < len(big) + eq:
                return pivot
            else:
                return qselect(small, k - eq - len(big))            
        
        return qselect(nums, k - 1)