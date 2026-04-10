class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Use a stack structure to hold (key, value)
        # empty arr [0,0,0,0,0]
        # loop from the back
        # if stack is empty: result[i] == 0
        # while (stack[-1][1] < temp[i]): pop (to hold it in an asending order)
        # if stack is empty: result[i] == 0
        # result[i] = stack[-1][0] - temp[i]
        

        stack = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures) - 1, -1, -1):
            if not stack:
                result[i] = 0
                stack.append((i, temperatures[i]))
            else:
                while stack and stack[-1][1] <= temperatures[i]:
                    stack.pop()
                if not stack:
                    result[i] = 0
                    stack.append((i, temperatures[i]))
                else:
                    result[i] = stack[-1][0] - i
                    stack.append((i, temperatures[i]))
        

        return result
