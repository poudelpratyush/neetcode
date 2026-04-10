class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            curr = target - nums[i]
            for j in range(i, len(nums)):
                if curr == nums[j] and i != j:
                    return [i, j]
        