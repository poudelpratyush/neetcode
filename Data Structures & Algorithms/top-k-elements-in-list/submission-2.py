
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # [1, 2, 2, 3, 3, 3] k = 2
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        # freq = [0[], 1[], 2[], 3[], 4[], 5[], 6[]]

        # O(n)
        for i in nums:
            if (i in count):
                count[i] += 1
            else:
                count[i] = 1 
        # {1:1, 2:2, 3:3}

        res =[]

        # O(n)
        for num, cnt in count.items():
            freq[cnt].append(num)
        # freq = [0[], 1[1], 2[2], 3[3], 4[], 5[], 6[]]

        res = []
        # O(n)
        for l in range(len(freq)-1, 0, -1):
            # O(1)
            for j in freq[l]:
                res.append(j)
                # Check if the number of k is reached
                if (len(res) == k):
                    return res


        # Time complexity: O(n) and memory O(n)=> because we create a hashmap
                
            
        

                 

            







            
