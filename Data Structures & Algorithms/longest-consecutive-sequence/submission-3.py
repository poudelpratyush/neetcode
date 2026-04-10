class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        # {2, 20, 4, 10, 3, 4, 5}

        maxCount = 1

        if len(nums) == 0:
            return 0
        
        for n in nums:
            count = 1
            curr = n
            change = True
            while (change == True):
                if (curr + 1 in s):
                    count += 1
                    curr += 1
                else:
                    change = False
                
                if (count > maxCount):
                    maxCount = count

        return maxCount

                




        
        

        
