class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # teaches about grouping/comparing values using hashmap
        
        # dict freq_list --> [] of anagrams
        dict_1 = defaultdict(list)

        for s in strs:
            # create frequency list
            freq_list = [0] * 26
            for char in s:
                freq_list[ord(char) - ord("a")] += 1
            
            # insert into hashmap
            dict_1[tuple(freq_list)].append(s)
        
        return list(dict_1.values())


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # my first thoughts:
        # m is number of strings
        # n is how long it takes to convert a string into a hashmap
        # put converted hashmap strings into larger hashmap; hashmap --> index

        
                
        
