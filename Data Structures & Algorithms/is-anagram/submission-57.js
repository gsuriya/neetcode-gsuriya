class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        const s_map = {}
        for (let c of s) {
            if (!s_map.hasOwnProperty(c)) {
                s_map[c] = 0
            }
            s_map[c] += 1
        }

        const t_map = {}
        for (let c of t) {
            if (!t_map.hasOwnProperty(c)) {
                t_map[c] = 0
            }
            t_map[c] += 1
        }

        // compare map equality
        if (Object.keys(s_map).length != Object.keys(t_map).length) {
            return false
        }

        // pairwise key
        for (let key of Object.keys(s_map)) {
            if (!t_map.hasOwnProperty(key) || t_map[key] != s_map[key]) {
                return false
            }
        }
        return true
    }
}
