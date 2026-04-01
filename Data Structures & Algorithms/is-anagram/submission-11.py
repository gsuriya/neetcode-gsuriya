class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = defaultdict(int)
        map2 = defaultdict(int)

        for char in s:
            map1[char] += 1
        for char in t:
            map2[char] += 1
        
        if len(map1) != len(map2):
            return False
        for key in map1.keys():
            if map1[key] != map2.get(key, 0):
                return False
        return True