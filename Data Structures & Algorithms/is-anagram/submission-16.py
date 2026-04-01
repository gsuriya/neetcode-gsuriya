class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # O(1) space --> CONSTANT size auxiliary DS's ALLOWED

        # freq_map for letters - O(1) space
        if len(s) != len(t):
            return False

        # letter --> freq
        map1 = defaultdict(int)
        map2 = defaultdict(int)

        for char in s:
            map1[char] += 1
        
        for char in t:
            map2[char] += 1
        
        # compare maps for equality
        for key in map1.keys():
            if map1[key] != map2[key]:
                return False
        return True