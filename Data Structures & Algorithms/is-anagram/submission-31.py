class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {} # letter --> freq

        for c in s:
            s_map[c] = s_map.get(c, 0) + 1
        
        t_map = defaultdict(int)

        for c in t:
            t_map[c] += 1
        
        # check equality of t_map and s_map
        if t_map.keys() != s_map.keys():
            return False
        
        for key in s_map:
            if s_map[key] != t_map.get(key, -1):
                return False
        
        return True
        
