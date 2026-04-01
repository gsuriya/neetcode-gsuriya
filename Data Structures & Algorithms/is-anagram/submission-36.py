class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = defaultdict(int)
        for c in s:
            s_map[c] += 1

        t_map = defaultdict(int)
        for c in t:
            t_map[c] += 1
        
        if len(s_map) != len(t_map):
            return False
        
        for key in s_map:
            if s_map[key] != t_map.get(key, -1):
                return False
        
        return True
        