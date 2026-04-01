class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # create freq_maps and compare

        s_map = {}
        for c in s:
            if c not in s_map:
                s_map[c] = 0
            s_map[c] += 1
        
        t_map = {}
        for c in t:
            if c not in t_map:
                t_map[c] = 0
            t_map[c] += 1
        
        # compare equality of freq_maps
        # 1. compare length  2. compare K-V pairs
        if len(s_map) != len(t_map):
            return False
        
        for key in s_map:
            if s_map[key] != t_map.get(key, -1):
                return False
        return True