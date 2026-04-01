class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # exact same chars --> # exact same FREQ of char
        # therefore, create freq_map or freq_list

        s_map = defaultdict(int)
        for char in s:
            s_map[char] += 1

        t_map = {}
        for char in t:
            t_map[char] = t_map.get(char, 0) + 1
        
        # compare equality of frequency maps
        if len(s_map) != len(t_map):
            return False
        
        for key in s_map:
            if s_map[key] != t_map.get(key, -1):
                return False
        
        return True

        #keys, values

        """
        r: 2, a: 1, c: 2, e: 1
        """
        
        
