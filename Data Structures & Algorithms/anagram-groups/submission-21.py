class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # strs share common freq_arr
        map1 = defaultdict(list) # freq_arr --> strs w/ that freq_arr

        # add each string in freq_arr buckets
        for s in strs:
            # create freq_arr
            freq_arr = [0] * 26
            for char in s:
                freq_arr[ord(char) - ord('a')] += 1
            map1[tuple(freq_arr)].append(s)
        
        return map1.values()
            




        
        
        
        
        
        
        
        
        
        
        
        
        
    
        
        
        
        
        
        
        
        # my first thoughts:
        # m is number of strings
        # n is how long it takes to convert a string into a hashmap
        # put converted hashmap strings into larger hashmap; hashmap --> index

        
                
        
