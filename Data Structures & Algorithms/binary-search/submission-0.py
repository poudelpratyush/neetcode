class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = r + l // 2
            if (nums[mid] == target):
                return mid
            elif (target > nums[mid]):
                l = mid + 1
            else:
                r = mid - 1
        
        if (l == r and nums[l] == target):
            return l
        else:
            return -1
