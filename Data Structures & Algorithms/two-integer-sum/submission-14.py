class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nSet = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if (diff in nSet.keys()):
                return [nSet[diff], i]
            nSet[nums[i]] = i
            
            