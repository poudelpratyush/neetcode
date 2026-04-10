class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s = {}
        for i in range(len(numbers)):
            curr = target - numbers[i]
            if (curr not in s):
                s[numbers[i]] = i
            else:
                return [s[curr] + 1, i + 1]
        return []

        