class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = defaultdict(int)
        map2 = defaultdict(int)

        for char in s:
            map1[char] += 1
        for char in t:
            map2[char] += 1
        
        return map1 == map2