class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # make freq_map for s and t
        s_map = defaultdict(int)
        for c in s:
            s_map[c] += 1

        t_map = defaultdict(int)
        for c in t:
            t_map[c] += 1

        # compare equality of hashmaps
        if len(s) != len(t):
            return False

        for key in s:
            if s_map[key] != t_map.get(key, -1):
                return False
        
        return True
        

        
        
