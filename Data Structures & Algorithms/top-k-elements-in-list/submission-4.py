class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        freq = [[] for i in range(len(nums)+1)]

        for num, values in count.items():
            freq[values].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if (len(res) == k):
                    return res