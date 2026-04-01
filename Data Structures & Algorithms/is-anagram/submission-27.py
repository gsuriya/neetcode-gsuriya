class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # create freq hashmaps and compare

        s_map = defaultdict(int)
        for char in s:
            s_map[char] += 1
        
        t_map = defaultdict(int)
        for char in t:
            t_map[char] += 1
        
        if len(t_map) != len(s_map):
            return False
        
        for key in s_map:
            if s_map[key] != t_map.get(key, -1):
                return False
        
        return True

