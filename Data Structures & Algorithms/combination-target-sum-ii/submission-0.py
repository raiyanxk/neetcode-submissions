class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        curr = []

        def dfs(i, curr_sum):

            if curr_sum > target:
                return
            
            if curr_sum == target:
                res.append(curr[:])
                return
            
            if i == len(candidates):
                return
            
            # add this number
            curr.append(candidates[i])
            dfs(i + 1, curr_sum + candidates[i])
            curr.pop()

            # skip this number
            i += 1
            while i < len(candidates) and candidates[i] == candidates[i - 1]:
                i += 1

            dfs(i, curr_sum)

        candidates.sort()
        dfs(0, 0)
        return res