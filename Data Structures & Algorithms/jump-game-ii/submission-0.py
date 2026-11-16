class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0

        start = 0
        end = 0

        while end < len(nums) - 1:
            new_start = end + 1
            new_end = end
            for i in range(start, end + 1):
                new_end = max(new_end, i + nums[i])
            
            start = new_start
            end = new_end
            res += 1

        return res 