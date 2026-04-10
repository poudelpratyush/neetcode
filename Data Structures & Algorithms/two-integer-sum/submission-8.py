class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # O(n)
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i

        for j in range(len(nums)):
            curr = target - nums[j]
            if (curr in d) and (d[curr] != j):
                return [j, d[curr]]