class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        groups = {} # tuple -> list

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1
            
            t = tuple(count)

            if t not in groups:
                groups[t] = []
            
            groups[t].append(s)
        
        res = []

        for group in groups:
            res.append([])

            for s in groups[group]:
                res[-1].append(s)
        
        return res

