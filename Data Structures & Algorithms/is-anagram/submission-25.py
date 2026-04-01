class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # create s_map
        s_map = {}
        for char in s:
            s_map[char] = s_map.get(char, 0) + 1

        # create t_map
        t_map = {}
        for char in t:
            t_map[char] = t_map.get(char, 0) + 1

        # return equality
        if len(s_map) != len(t_map):
            return False
        
        for key in s_map:
            if s_map[key] != t_map.get(key, -1):
                return False
        
        return True


