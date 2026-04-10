class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxCount = 0
        for num in nums:
            if (num - 1 not in s):
                count = 1
                curr = num
                notDone = True
                while (notDone == True):
                    if (curr + 1 in s):
                        count += 1
                        curr += 1
                    else:
                        notDone = False
                        if (count > maxCount):
                            maxCount = count
        return maxCount


                




        
        

        
