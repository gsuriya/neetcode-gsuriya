class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list) # freq_list --> str w/ that frq_list
        
        # for each string, create frequency list
        for s in strs:
            freq_list = [0] * 26
            for c in s:
                freq_list[ord(c) - ord('a')] += 1

            anagram_map[tuple(freq_list)].append(s)

        # return map.value
        return anagram_map.values()