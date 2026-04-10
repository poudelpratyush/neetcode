class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        
        prefix = [1] * n
        for i in range(1, n):
            prefix[i] = nums[i-1] * prefix[i-1]

        #[1, 1, 2, 8]

        postfix = [1] * n
        for j in range(n-2,-1, -1):
            postfix[j] = postfix[j+1] * nums[j+1]

        # [48,24, 6, 1]
        
        res = [1] *n

        for i in range(n):
            res[i] = postfix[i] * prefix[i]

        return res

            
            
        



        

        
            

        




        


        



        
                


            
     
                
        

        