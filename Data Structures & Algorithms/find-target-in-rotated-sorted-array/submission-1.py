class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Main goal at the start: Finding the pivot point (lowest value in the array)
        # Binary search on nums
        # if M > R: L = M + 1
        # else M < R: R = M
        # After finding the middle index
        # Run a basic binary search from 0 - pivot index
        # and pivot index - len(nums)


        # Find the pivot index
        l, r = 0, len(nums) - 1
        pI = 0
        while l <= r:
            if l == r:
                pI = l
                break
            else:
                m = (l + r) // 2
                if nums[m] > nums[r]:
                    l = m + 1
                else:
                    r = m

        # From 0 to pivot
        l1, r1 = 0, pI - 1
        while l1 <= r1:
            m1 = (l1 + r1) // 2
            if target < nums[m1]:
                r1 = m1 - 1
            elif target > nums[m1]:
                l1 = m1 + 1
            else:
                return m1

        # From pivot to the end
        l2, r2 = pI, len(nums) - 1
        while l2 <= r2:
            m2 = (l2 + r2) // 2
            if target < nums[m2]:
                r2 = m2 - 1
            elif target > nums[m2]:
                l2 = m2 + 1
            else:
                return m2
        
        return -1
        
            
        



        

                
        