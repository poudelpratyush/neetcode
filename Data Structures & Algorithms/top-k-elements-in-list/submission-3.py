from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        hs = defaultdict(int)
        
        for num in nums:
            hs[num] += 1



        for i in range(k):
            highest = nums[0]
            for n in nums:
                if (n in hs and hs[n] > hs[highest]):
                    highest = n
            res.append(highest)
            hs.pop(highest)
        
        return res



            







            
