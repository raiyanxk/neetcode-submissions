class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        buckets = [[] for _ in range(len(nums) + 1)]

        counts = collections.defaultdict(int)

        for num in nums:
            counts[num] += 1
        
        for c in counts:
            buckets[counts[c]].append(c)
        
        res = []
        i = len(buckets) - 1

        while k > 0:
            if buckets[i]:
                for c in buckets[i]:
                    res.append(c)
                    k -= 1
            i -= 1
        
        return res

