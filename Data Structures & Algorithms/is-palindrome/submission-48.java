class Solution {
    public boolean isPalindrome(String s) {
        int L = 0;
        int R = s.length()-1;

        while (L <= R) {
            // move L to next alphanumeric
            while (L < R && !isAlphanumeric(s.charAt(L))) {
                L++;
            }

            // move R to next alphanumeric
            while (L < R && !isAlphanumeric(s.charAt(R))) {
                R--;
            }

            // check equality
            if (Character.toLowerCase(s.charAt(L)) != Character.toLowerCase(s.charAt(R))) {
                return false;
            }

            // increment pointers
            L++;
            R--;
        }

        return true;
    }
    

    public boolean isAlphanumeric(char c) {
    if (('A' <= c && c <= 'Z') ||
        ('a' <= c && c <= 'z') ||
        ('0' <= c && c <= '9')) {
        return true;
    } else {
        return false;
    }
    }

}
