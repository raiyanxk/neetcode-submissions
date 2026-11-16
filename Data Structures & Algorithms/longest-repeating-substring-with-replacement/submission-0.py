class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        window = [0] * 26
        maxf = 0

        for r in range(len(s)):
            char = s[r]
            window[ord(char) - ord('A')] += 1
            maxf = max(maxf, window[ord(char) - ord('A')])

            while ((r - l + 1) - maxf > k):
                window[ord(s[l]) - ord('A')] -= 1
                l += 1
        
        return r - l + 1 
        