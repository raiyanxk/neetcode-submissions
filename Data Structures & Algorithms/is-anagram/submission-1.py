class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        s_c = [0] * 26
        t_c = [0] * 26

        for c1, c2 in zip(s, t):
            s_c[ord(c1) - ord('a')] += 1
            t_c[ord(c2) - ord('a')] += 1

        for i in range(26):
            if s_c[i] != t_c[i]:
                return False
        
        return True