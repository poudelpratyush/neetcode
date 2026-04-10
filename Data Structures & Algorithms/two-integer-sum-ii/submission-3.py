class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # [1, 2, 3, 4] # 3

        # create two pointer one for left and one for right
        # run a while loop while l < r
        # 1. check if val[l] + val[r] == target
        #       if yes return [l + 1, r + 1]
        # 2. check if val[l] + val[r] > target
        #       r -= 1
        # 3. check if val[l] - val[r] < target
        #       l += 1
        # return the current l + 1, r + 1

        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1
        
        return []