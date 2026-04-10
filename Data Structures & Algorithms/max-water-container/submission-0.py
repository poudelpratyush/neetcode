class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxArea = 0
        while (l < r):
            tempL = l
            tempR = r
            currHeight = 0
            currArea = 0
            if (heights[tempL] < heights[tempR]):
                currHeight = heights[tempL]
                l += 1
            elif (heights[tempL] > heights[tempR]):
                currHeight = heights[tempR]
                r -= 1
            else:
                currHeight = heights[tempR]
                leftCheck = heights[tempL + 1]
                rightCheck = heights[tempR - 1]
                if (rightCheck > leftCheck):
                    r -= 1
                else:
                    l += 1

            currArea = ((tempR - tempL) * currHeight)
            if (maxArea < currArea):
                maxArea = currArea

        return maxArea

            


        