class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1_c = [0] * 26
        s2_c = [0] * 26
        matches = 0

        for c1,c2 in zip(s1, s2):
            s1_c[ord(c1) - ord('a')] += 1
            s2_c[ord(c2) - ord('a')] += 1

        for i in range(26):
            if s1_c[i] == s2_c[i]:
                matches += 1
        
        if matches == 26:
            return True

        l = 0

        for r in range(len(s1), len(s2)):
            l_char = s2[l]
            r_char = s2[r]

            # we want to remove l_char
            if s2_c[ord(l_char) - ord('a')] == s1_c[ord(l_char) - ord('a')]:
                matches -= 1
            elif s2_c[ord(l_char) - ord('a')] == s1_c[ord(l_char) - ord('a')] + 1:
                matches += 1

            s2_c[ord(l_char) - ord('a')] -= 1

            l += 1

            # we want to add r_char
            if s2_c[ord(r_char) - ord('a')] == s1_c[ord(r_char) - ord('a')]:
                matches -= 1
            elif s2_c[ord(r_char) - ord('a')] + 1 == s1_c[ord(r_char) - ord('a')]:
                matches += 1
            
            s2_c[ord(r_char) - ord('a')] += 1


            if matches == 26:
                return True

        return False       