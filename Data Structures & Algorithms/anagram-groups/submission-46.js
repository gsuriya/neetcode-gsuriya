class Solution {
    /**
     * 
     * anagram_map = {} # freq_list --> list of words w/ that freq_list
     * 
     */
    groupAnagrams(strs) {
        const anagram_map = {} // str(freq_list) --> list of words w/ that freq_list

        for (const s of strs) {
            // create freq_list
            const freq_list = new Array(26).fill(0)
            for (const c of s) {
                freq_list[c.charCodeAt() - 'a'.charCodeAt()] += 1
            }
            
            // insert into anagram_map
            const key = freq_list.join(',')
            if (!anagram_map.hasOwnProperty(key)) {
                anagram_map[key] = []
            }
            anagram_map[key].push(s)

        }

        return Object.values(anagram_map)
    }
}
