class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """

        for each s
        - create freq_list
        - use it as key to insert into hashmap

        - return map.values()

        """

        anagram_map = defaultdict(list) # freq_list --> [list of words w/ that list]

        for s in strs:
            # create freq_list
            freq_list = [0] * 26
            for c in s:
                freq_list[ord(c.lower())-ord('a')] += 1

            # insert into map
            anagram_map[tuple(freq_list)].append(s)

        return list(anagram_map.values())