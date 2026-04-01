class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # compare freq maps

        s_map = defaultdict(int)
        for char in s:
            s_map[char] += 1
        

        t_map = {}
        for char in t:
            t_map[char] = t_map.get(char, 0) + 1
        

        return t_map == s_map
