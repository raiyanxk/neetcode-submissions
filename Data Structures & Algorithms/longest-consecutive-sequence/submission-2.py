class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numbers = set(nums)

        res = 0

        for num in numbers:
            if num - 1 in numbers:
                continue
            
            curr = 0
            n = num

            while n in numbers:
                curr += 1
                n += 1

            res = max(res, curr)
        
        return res 