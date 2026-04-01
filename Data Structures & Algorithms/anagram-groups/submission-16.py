class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # freq_list --> strs w/ that list
        # return map.values() as a list
        anagram_map = defaultdict(list)

        # all the strings have a common freq_list
        # can't use freq_map cus maps are mutable, can't be used as keys in map

        
        for s in strs:
            # create freq_list
            freq_list = [0] * 26
            for char in s:
                freq_list[ord(char) - ord("a")] += 1
            # s in map
            anagram_map[tuple(freq_list)].append(s)

        return anagram_map.values()

        return anagram_map.values()






        
        
        
        
        
        
        
        
        
        
        
        
        
    
        
        
        
        
        
        
        
        # my first thoughts:
        # m is number of strings
        # n is how long it takes to convert a string into a hashmap
        # put converted hashmap strings into larger hashmap; hashmap --> index

        
                
        
