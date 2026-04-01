class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # teaches about grouping/comparing values using hashmap

        # mapping freq_map --> string items
        dict_1 = defaultdict(list)

        #common att string share is frequency hashmap
        for s in strs:
            #create frequency hashmap
            freq_map = defaultdict(int)
            for char in s:
                freq_map[char] += 1
            
            # insert common att (freq_map) as key
            dict_1[tuple(sorted(freq_map.items()))].append(s)
        
        return list(dict_1.values())


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # my first thoughts:
        # m is number of strings
        # n is how long it takes to convert a string into a hashmap
        # put converted hashmap strings into larger hashmap; hashmap --> index

        
                
        
