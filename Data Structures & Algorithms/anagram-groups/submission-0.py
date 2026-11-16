class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []

        mapping = {}

        for string in strs:
            counts = [0] * 26
            
            for i in range(len(string)):
                counts[ord(string[i]) - ord('a')] += 1
            
            tup = tuple(counts)

            if tup not in mapping:
                mapping[tup] = []
            
            mapping[tup].append(string)
        
        for word in mapping:
            count = [string for string in mapping[word]]
            res.append(count[:])

        return res 




        