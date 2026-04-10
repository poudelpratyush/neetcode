class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i in range(len(nums)):
            s[nums[i]] = i

        # [1, 3, 4, 2] target = 6
        # s = {1:0, 3:1, 4:2, 2:3}
        # [1,1]

        for j in range(len(nums)):
            curr = target - nums[j]
            if (curr in s) and (s[curr] != j):
                return [j, s[curr]]