class Solution {
    public int getSum(int a, int b) {
        /*

                    a
                    b
                    --
            new_a = XOR (a^b)
            new_b = carry (a&b << 1) --> if this is != 0, then repeat w/ new a and b


        */

        // carry becomes the new b, repeat until carry is not 0
        while (b != 0) {
            int new_a = a ^ b; // sum
            int new_b = (a & b) << 1; // carry

            a = new_a;
            b = new_b;
        }

        return a;

    }
}
