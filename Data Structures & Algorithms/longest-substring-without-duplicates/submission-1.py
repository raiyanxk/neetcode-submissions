class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        window = set()
        l = 0
        res = 0

        for r in range(len(s)):
            c = s[r]

            while c in window:
                l_c = s[l]
                window.remove(l_c)
                l += 1
            
            window.add(c)
            res = max(res, r - l + 1)

        return res
