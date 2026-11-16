class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_counts = [0] * 26
        s2_counts = [0] * 26
        matches = 0

        for i in range(len(s1)):
            s1_counts[ord(s1[i]) - ord('a')] += 1
            s2_counts[ord(s2[i]) - ord('a')] += 1

        for i in range(26):
            if s1_counts[i] == s2_counts[i]:
                matches += 1
        
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            left_char = s2[r - len(s1)]
            right_char = s2[r]

            s2_counts[ord(right_char) - ord('a')] += 1
            s2_counts[ord(left_char) - ord('a')] -= 1

            if right_char == left_char:
                continue
            
            if s2_counts[ord(right_char) - ord('a')] == s1_counts[ord(right_char) - ord('a')]:
                matches += 1
            elif s2_counts[ord(right_char) - ord('a')] == s1_counts[ord(right_char) - ord('a')] + 1:
                matches -= 1
            
            if s2_counts[ord(left_char) - ord('a')] == s1_counts[ord(left_char) - ord('a')]:
                matches += 1
            elif s2_counts[ord(left_char) - ord('a')] + 1 == s1_counts[ord(left_char) - ord('a')]:
                matches -= 1

        
        return matches == 26