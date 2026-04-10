class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prev = []
        post = []

        # prev arr
        prevCount = 1
        for i in range(len(nums)):
            if (i != 0):
                prevCount *= nums[i-1]
            prev.append(prevCount)

        # [1, 1, 2, 8]

        # post arr
        postCount = 1
        for j in range(len(nums)-1, -1, -1):
            if (j != len(nums)-1):
                postCount *= nums[j+1]
            post.append(postCount)

        res = []
        for k in range(len(nums)):
            res.append(prev[k] * post[len(nums) - 1 - k])

        return res



            
        



        

        
            

        




        


        



        
                


            
     
                
        

        