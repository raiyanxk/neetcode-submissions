class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        buckets = [[] for _ in range(len(nums) + 1)]

        counts = collections.defaultdict(int)

        res = []

        for num in nums:
            counts[num] += 1
        
        for num in counts:
            count = counts[num]
            buckets[count].append(num)
        

        index = len(buckets) - 1

        while k > 0:
            if buckets[index]:
                for item in buckets[index]:
                    res.append(item)
                    k -= 1
            
            index -= 1

    
        return res 
                