class Solution:
    def isAnagram(self, s: str, t: str) -> bool:


        # O(n)
        mapOne = {}
        mapTwo = {}
        if (len(s) != len(t)):
            return False
        else:
            for i in range(len(s)): # O(n)
                if s[i] in mapOne:
                    mapOne[s[i]] += 1
                else:
                    mapOne[s[i]] = 1
            for j in range(len(s)): # O(n)
                if t[j] in mapTwo:
                    mapTwo[t[j]] += 1
                else:
                    mapTwo[t[j]] = 1
        return mapOne == mapTwo
        
