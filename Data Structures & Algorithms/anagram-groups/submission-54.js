class Solution {
    /**
     
     for each string, create freq_list
     - insert into anagram_map[freq_list].append(s)

     */
    groupAnagrams(strs) {
        const anagram_map = {} // freq_list --> list of strings w/ that freq_list

        for (const s of strs) {
            // create freq_list and insert into map
            const freq_list = new Array(26).fill(0)
            for (const c of s) {
                freq_list[c.toLowerCase().charCodeAt() - 'a'.charCodeAt()] += 1
            }

            const key = freq_list.join(',')
            if (!anagram_map.hasOwnProperty(key)) {
                anagram_map[key] = []
            }
            
            anagram_map[key].push(s)
        }

        return Object.values(anagram_map)
    }
}





