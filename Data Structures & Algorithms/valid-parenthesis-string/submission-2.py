class Solution:
    def checkValidString(self, s: str) -> bool:
        """

        normally would hv only 1 net variable, but w/ * now we hv a RANGE OF POSSIBILITIES

        net_min --> increment on "(", decrement on ")", BUT decrement on "*"
        net_max --> increment on "(", decrement on ")", BUT increment on "*"

        if all *** then net_min negative --> make sure net_min floor is 0
        net_max can keep decreasing as more ))) and can become neg --> this var tracks ))( 

        """
        net_min, net_max = 0, 0

        for c in s:
            if c == "(":
                net_min += 1
                net_max += 1
            elif c == ")":
                net_min -= 1
                net_max -= 1
            elif c == "*":
                net_min -= 1
                net_max += 1
            net_min = max(0, net_min)

            if net_max < 0: return False # ))((
        
        return net_min == 0





            