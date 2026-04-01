class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # anagram means same freq map 
        s_map = defaultdict(int)
        for char in s:
            s_map[char] += 1

        t_map = defaultdict(int)
        for char in t:
            t_map[char] += 1
        
        # check for equality

        if len(s_map) != len(t_map):
            return False

        # now that keys equality good, loop over one of their keys
        for key in s_map.keys():
            if s_map[key] != t_map.get(key, -1):
                return False
        
        return True