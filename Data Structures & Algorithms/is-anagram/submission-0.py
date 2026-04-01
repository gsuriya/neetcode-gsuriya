class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict, t_dict = {}, {}

        # put strings into frequency hashmaps
        for char in s:
            s_dict[char] = s_dict.get(char, 0) + 1
        
        for char in t:
            t_dict[char] = t_dict.get(char, 0) + 1

        # compare hashmaps for equality
        for key in s_dict.keys(): # equal hashmaps should have same keys
            if s_dict.get(key, 1) != t_dict.get(key, 0):
                return False
        
        return True
