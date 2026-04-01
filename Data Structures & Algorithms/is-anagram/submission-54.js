class Solution {
    /**
     * create freq_maps
     * compare equality
     */
    isAnagram(s, t) {
        // create freq_maps
        const s_freq_map = {}
        for (const c of s) {
            if (!s_freq_map.hasOwnProperty(c)) {
                s_freq_map[c] = 0
            }
            s_freq_map[c] += 1
        }

        const t_freq_map = {}
        for (const c of t) {
            if (!t_freq_map.hasOwnProperty(c)) {
                t_freq_map[c] = 0
            }
            t_freq_map[c] += 1
        }

        // compare equality
        if (Object.keys(s_freq_map).length != Object.keys(t_freq_map).length) {
            return false;
        }
        for (const key of Object.keys(s_freq_map)) {
            if (s_freq_map[key] != t_freq_map[key]) {
                return false;
            }
        }
        return true;
    }
}






