class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = []

        for i in range(len(temperatures) - 1, -1, -1):
            curr = temperatures[i]
            toInsert = [curr, i]
            if len(stack) == 0:
                res.append(0)
            else:
                while (len(stack) != 0 and stack[-1][0] <= curr):
                    stack.pop()
                if len(stack) == 0:
                    res.append(0)
                else:
                    diff = stack[-1][1] - i
                    res.append(diff)
            stack.append(toInsert)
        res.reverse()
        return res