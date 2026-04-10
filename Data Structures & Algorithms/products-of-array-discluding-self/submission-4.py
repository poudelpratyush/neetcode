class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prev = []

        # prev arr
        prevCount = 1
        for i in range(len(nums)):
            if (i != 0):
                prevCount *= nums[i-1]
            prev.append(prevCount)

        # [1, 1, 2, 8]

        postCount = 1
        for j in range(len(nums)-1, -1, -1):
            if (j != len(nums)-1):
                postCount *= nums[j+1]
            prev[j] *= postCount

        return prev



            
        



        

        
            

        




        


        



        
                


            
     
                
        

        