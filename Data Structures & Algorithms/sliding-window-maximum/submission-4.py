class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        q = collections.deque()

        for i, num in enumerate(nums):
            
            while q and q[-1][0] < num:
                q.pop()

            q.append((num, i))
            
            if i + 1 >= k:

                while q[0][1] <= i - k:
                    q.popleft()
                
                res.append(q[0][0])

        return res