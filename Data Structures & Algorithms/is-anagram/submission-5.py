class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map1 = {}
        map2 = {}

        for char in s:
            map1[char] = map1.get(char, 0) + 1
        for char in t:
            map2[char] = map2.get(char, 0) + 1

        for key in map1.keys():
            if map1[key] != map2.get(key, 0):
                return False
        
        return True


