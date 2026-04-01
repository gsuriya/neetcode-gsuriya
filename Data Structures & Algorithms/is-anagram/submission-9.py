class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_1, count_2 = [0] * 26, [0] * 26

        for char in s:
            count_1[ord(char) - ord("a")] += 1
        for char in t:
            count_2[ord(char) - ord("a")] += 1

        return count_1 == count_2