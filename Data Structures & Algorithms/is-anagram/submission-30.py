class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {} # letter --> freq

        for c in s:
            s_map[c] = s_map.get(c, 0) + 1
        
        t_map = defaultdict(int)

        for c in t:
            t_map[c] += 1
        
        return t_map == s_map
        
