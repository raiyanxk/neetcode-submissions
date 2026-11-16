class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        curr = []
        res = []

        def backtrack(i, curr_sum):
            
            if curr_sum == target:
                res.append(curr[:])
                return
            
            if i == len(nums) or curr_sum > target:
                return 
            
            # add current element, and stay
            curr.append(nums[i])
            backtrack(i, curr_sum + nums[i])
            curr.pop()

            # skip current element
            backtrack(i + 1, curr_sum)
        
        backtrack(0, 0)

        return res