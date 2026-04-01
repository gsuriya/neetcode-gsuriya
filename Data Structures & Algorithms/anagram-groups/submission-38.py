class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        freq_list --> words w/ that freq_list

        """
        anagram_map = defaultdict(list)

        for s in strs:
            # create freq_list
            freq_list = [0] * 26
            
            for c in s:
                freq_list[ord(c) - ord('a')] += 1
            
            anagram_map[tuple(freq_list)].append(s)
        
        return list(anagram_map.values())

            
            

        