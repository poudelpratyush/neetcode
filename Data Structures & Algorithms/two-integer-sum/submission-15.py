class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # one loop
        nSet = {} # values:keys
        for i in range(len(nums)):
            # find the difference first
            diff = target - nums[i]
            # check if the difference is in the hashset
            # if it is we return the index of the one in the set
            # and then the current index
            if (diff in nSet):
                return [nSet[diff], i]
            # if not we add to the hashset
            nSet[nums[i]] = i

        # two loop
        jSet = {}
        for j in range(len(nums)):
            jSet[nums[j]] = j

        for k in range(len(nums)):
            diff = target - nums[k]
            if (diff in jSet and jSet[diff] != k):
                return [k, jSet[diff]]
            
            
            
            