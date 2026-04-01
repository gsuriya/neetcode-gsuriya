class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_1, count_2 = [0] * 26, [0] * 26

        for char in s:
            count_1[ord(char) - ord("a")] += 1
        for char in t:
            count_2[ord(char) - ord("a")] += 1

        if len(count_1) != len(count_2):
            return False
        for i in range(len(count_1)):
            if count_1[i] != count_2[i]:
                return False
        
        return True