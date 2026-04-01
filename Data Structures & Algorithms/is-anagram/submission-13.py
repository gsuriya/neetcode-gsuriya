class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # create 2 maps: letters --> frequency
        map1 = {}
        map2 = {}

        # populate the maps
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            map1[s[i]] = map1.get(s[i], 0) + 1
            map2[t[i]] = map2.get(t[i], 0) + 1
        
        return map1 == map2