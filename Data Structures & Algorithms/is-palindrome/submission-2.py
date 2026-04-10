class Solution:
    def isPalindrome(self, s: str) -> bool:

        # get the end index and the first index
        l = 0
        r = len(s) - 1

        # loop while they dont cross each other
        # since they only want us to have alphanumeric values 
        # we use a helper function to see that
        while (l < r):
            # while the value at our left or right currently isnt 
            # alphanumemric we are going to keep going forward or back
            # or till we get to the end or the start
            while l < r and not (self.isAlphanumeric(s[l])):
                l += 1
            while r > l and not (self.isAlphanumeric(s[r])):
                r -= 1

            # then we check if the lowercase value at the left is
            # equal to the lowercase value at the right
            # if not we return false
            if (s[l].lower() != s[r].lower()):
                return False
            
            # then we increment from the back and the front
            l += 1
            r -= 1

        return True


    # helper function check if the curr char lies within a certain ascii value
    def isAlphanumeric(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('0') <= ord(c) <= ord('9') or
                ord('a') <= ord(c) <= ord('z')
                )