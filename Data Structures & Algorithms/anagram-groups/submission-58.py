class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """

        for each s
        - create freq_list
        - insert tuple(freq_list) into anagram_map

        anagram_map # freq_list --> list of strings w/ that freq_list

        """
        anagram_map = defaultdict(list) # freq_list --> list of strings w/ that freq_list

        for s in strs:
            # create freq_list
            freq_list = [0] * 26
            for c in s:
                freq_list[ord(c.lower())-ord('a')] += 1

            # insert into anagram_map
            anagram_map[tuple(freq_list)].append(s)

        # return anagram_map.values
        return list(anagram_map.values())