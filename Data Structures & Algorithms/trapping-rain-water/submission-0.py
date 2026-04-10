class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = []
        postfix = []
        area = 0

        currMaxL = 0
        for i in range(len(height)):
            prefix.append(currMaxL)
            if (height[i] > currMaxL):
                currMaxL = height[i]

        currMaxR = 0
        for i in range(len(height) - 1, -1, -1):
            postfix.append(currMaxR)
            if (height[i] > currMaxR):
                currMaxR = height[i]

        postfix.reverse()

        for i in range(len(height)):
            pA = min(prefix[i], postfix[i]) - height[i]
            if (pA > 0):
                area += pA

        return area
         
                



        