class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Q: can I do this problem w/ a stack/queue?

        # A: use monotonically increasing stack

        """
        max_profit = max(top - bottom , max_profit)

        technically using a arraylist b/c accessing arr[0] elem
        stack = [

            1
        ]
        """
        max_profit = 0
        array_list = []

        for p in prices:
            while array_list and array_list[-1] > p:
                array_list.pop()
            array_list.append(p)
            max_profit = max(p - array_list[0] , max_profit)

        return max_profit
        