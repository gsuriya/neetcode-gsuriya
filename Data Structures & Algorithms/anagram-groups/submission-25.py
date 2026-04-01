class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # anagrams have a common freq_list
        # map: freq_list --> str w/ that freq_list
        anagram_map = defaultdict(list)

        for s in strs:
            # construct freq_list for s
            freq_list = [0] * 26
            for char in s:
                freq_list[ord(char.lower()) - ord("a")] += 1
            anagram_map[tuple(freq_list)].append(s)

        return anagram_map.values() 






        
        
        
        
        
        
        
        
        
        
        
        
        
    
        
        
        
        
        
        
        
        # my first thoughts:
        # m is number of strings
        # n is how long it takes to convert a string into a hashmap
        # put converted hashmap strings into larger hashmap; hashmap --> index

        
                
        
