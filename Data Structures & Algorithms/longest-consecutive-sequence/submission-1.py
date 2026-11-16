class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        res = 0

        for num in nums:
            length = 0
            curr = num
            if num - 1 not in seen:
                while curr in seen:
                    curr += 1
                    length += 1
            
            res = max(length, res)

        return res 