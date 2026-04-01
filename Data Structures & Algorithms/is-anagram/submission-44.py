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
        return s_map == t_map