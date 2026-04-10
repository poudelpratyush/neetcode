class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # Other methods in notes
        # Using Hash Set

        s = set()

        for i in nums:
            if i in s:
                return True
            else:
                s.add(i)
        return False


