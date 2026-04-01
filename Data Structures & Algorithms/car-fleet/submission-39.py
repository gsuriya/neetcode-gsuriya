import math
from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        steps = []
        for p, s in sorted(zip(position, speed), reverse=True):
            steps.append((target - p) / s)  # ceil not needed

        stack = []
        for t in steps:
            if not stack or t > stack[-1]:
                stack.append(t)

        return len(stack)