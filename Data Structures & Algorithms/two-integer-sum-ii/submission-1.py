class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers)-1
        s = set(numbers)

        while (i < j):
            currI = target - numbers[i]
            currJ = target - numbers[j]
            if (currI not in s):
                i += 1
            if (currJ not in s):
                j -= 1
            if (currI + currJ == target):
                return [i+1, j+1]
        