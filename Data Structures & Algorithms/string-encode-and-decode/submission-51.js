class Solution {
    /**
     * FORMAT: length # string
     * 
     * [hi, bye, yo]
     * 
     * 2#hi3#bye2#yo
     * 
     */
    encode(strs) {
        let res = ""

        for (const s of strs) {
            res += String(s.length) + "#"
            for (const c of s) {
                res += c
            }
        }

        return res
    }

    /**
     *           i
     * str = 2#hi3#bye2#yo
     * 
     * [hi, bye, yo]
     */
    decode(str) {
        const res = []

        let i = 0
        while (i < str.length) {
            // extract length
            let length = ""
            while (str[i] != "#") {
                length += str[i]
                i += 1
            }
            length = Number(length)
            i += 1

            // extract string using length
            let s = ""
            while (length != 0) {
                s += str[i]
                length -= 1
                i += 1
            }
            res.push(s)
        }

        return res
    }
}





