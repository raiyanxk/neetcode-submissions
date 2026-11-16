class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        counts = {}
        res = []

        for num in nums:
            if num not in counts:
                counts[num] = 0
            counts[num] += 1
        
        for num in counts:
            count = counts[num]
            buckets[count].append(num)
        
        r = len(buckets) - 1

        while k > 0:
            for item in buckets[r]:
                res.append(item)
                k -= 1

            r -= 1
        
        return res 
        