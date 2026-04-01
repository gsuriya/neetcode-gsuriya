class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = defaultdict(int)
        for c in s:
            s_map[c] += 1
        
        t_map = defaultdict(int)
        for c in t:
            t_map[c] += 1
        
        # compare equality of maps
        if len(s_map) != len(t_map):
            return False
        
        for c in s_map:
            if s_map[c] != t_map.get(c, -1):
                return False
        
        return True
