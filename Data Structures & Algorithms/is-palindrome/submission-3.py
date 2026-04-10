class Solution:
    def isPalindrome(self, s: str) -> bool:
        # create two pointers front and back
        # keep changing it until the l <= r
        # if a character at l or right is not alphanumeric
        # make it go left until it is or right until its not
        # if the characters are not true return false
        # else return true
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while l < r and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))