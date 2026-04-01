class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # O(1) space --> CONSTANT size auxiliary DS's ALLOWED

        # freq_map for letters - O(1) space
        if len(s) != len(t):
            return False

        # letter --> freq
        map1 = defaultdict(int)
        map2 = defaultdict(int)

        for i in range(len(s)):
            map1[s[i]] += 1
            map2[t[i]] += 1
        
        # compare maps for equality
        for key in map1.keys():
            if map1[key] != map2[key]:
                return False
        return True