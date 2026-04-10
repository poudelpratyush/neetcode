class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        #nums: [1, 2, 4, 6]
        #res: [2*4*6, 1*4*6, 1*2*6, 1*2*4]
        res = []

        for i in range(len(nums)):
            sum = 1
            for j in range(len(nums)):
                if (i!=j):
                    sum *= nums[j] 
            res.append(sum)

        return res


        


        



        
                


            
     
                
        

        