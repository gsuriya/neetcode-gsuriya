class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # map: freq_tuple --> list of strs w/ that freq_tuple

        # for each str, create a freq_tuple
        # then insert freq_tuple into map: map[freq_tuple].append(s)

        anagram_map = defaultdict(list)

        for s in strs:
            freq_list = [0] * 26
            for c in s:
                freq_list[ord(c.lower())-ord('a')] += 1
            freq_tuple = tuple(freq_list)
            anagram_map[freq_tuple].append(s)
        
        return anagram_map.values()









        
        
        
        
        
        
        
        
        
        
        
        
        
    
        
        
        
        
        
        
        
        # my first thoughts:
        # m is number of strings
        # n is how long it takes to convert a string into a hashmap
        # put converted hashmap strings into larger hashmap; hashmap --> index

        
                
        
