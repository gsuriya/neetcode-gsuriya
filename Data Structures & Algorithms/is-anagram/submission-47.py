class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # create freq maps of s and t
        s_map = {}
        for c in s:
            s_map[c] = s_map.get(c, 0) + 1

        t_map = defaultdict(int)

        for c in t:
            t_map[c] += 1

        # compare equality of maps
        if len(s_map) != len(t_map):
            return False
        
        for key in s_map:
            if s_map[key] != t_map.get(key, -1):
                return False
        
        return True