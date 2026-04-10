class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        # Brute force => O(n^2)
        for i in range(len(nums)): # O(n)
            for j in range(i+1, len(nums)): # O(n)
                if nums[i] == nums[j]: # O(1)
                    return True
        return False
        '''

        '''
        # Sorting => O(n log n)
        numsSorted = sorted(nums) # O(n log n)
        for i in range(len(numsSorted)): # O(n)
            if (i < len(numsSorted)-1):
                if numsSorted[i] == numsSorted[i+1]:
                    return True
        return False
        '''

        # Using Hash Set

        s = set()

        for i in nums:
            if i in s:
                return True
            else:
                s.add(i)
        return False


