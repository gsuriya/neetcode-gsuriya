class Solution:
    def checkValidString(self, s: str) -> bool:
        """

        **** --> net_min floored at 0

        ))(( --> so use net_max being negative to detect this scenario

        """
        net_min, net_max = 0, 0

        for c in s:
            if c == "(":
                net_min += 1
                net_max += 1
            elif c == ")":
                net_min = max(0, net_min - 1) # NEED FLOORING IN BOTH PLACEES. net_max can be higher than net_min rn so it wont get caughtin the if statement for false thigns
                net_max -= 1
            
            # where they differ
            elif c == "*":
                net_min = max(0, net_min - 1)
                net_max += 1
            
            if net_max < 0:
                return False
        
        return net_min == 0



        