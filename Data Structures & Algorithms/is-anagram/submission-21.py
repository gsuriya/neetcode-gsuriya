class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # anagrams --> same freq_list or freq_map
        s_map = defaultdict(int)
        for char in s:
            s_map[char] += 1

        t_map = defaultdict(int)
        for char in t:
            t_map[char] += 1

        # check maps for equality
        if len(s_map.keys()) != len(t_map.keys()):
            return False
        
        for key in s_map.keys():
            if s_map[key] != t_map.get(key, 0):
                return False
        
        return True