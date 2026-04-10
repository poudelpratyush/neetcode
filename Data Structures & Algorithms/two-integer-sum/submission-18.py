class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a hashmap that maps the num:index
        # {3:0, 4:1, 5:2, 6: 3}
        # loop through the nums
        # for each number set diff =  target - number
        # check if (diff is in the hashmap and index for diff != index for number)
        # if true return [number index, diff index]
        # O(n) time
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i

        for j in range(len(nums)):
            curr = target - nums[j]
            if (curr in d) and (d[curr] != j):
                return [j, d[curr]]

        
        
        
            
            