class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        # anagrams have common freq_list
        for s in strs:
            # create freq_list
            freq_list = [0] * 26
            for c in s:
                freq_list[ord(c) - ord('a')] += 1
            anagram_map[tuple(freq_list)].append(s)

        return anagram_map.values() 







        
        
        
        
        
        
        
        
        
        
        
        
        
    
        
        
        
        
        
        
        
        # my first thoughts:
        # m is number of strings
        # n is how long it takes to convert a string into a hashmap
        # put converted hashmap strings into larger hashmap; hashmap --> index

        
                
        
