class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counts = collections.defaultdict(int)

        for c in s:
            counts[c] += 1
        
        res = []
        l = 0
        window = set()

        for r in range(len(s)):
            char = s[r]
            
            if char not in window:
                window.add(char)
            
            counts[char] -= 1
            if counts[char] == 0:
                window.remove(char)
            
            if len(window) == 0:
                res.append(r - l + 1)
                l = r + 1

        return res 