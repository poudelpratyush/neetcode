class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = {}
        second = {}

        if len(s) != len(t):
            return False

        for i in s:
            if i not in first:
                first[i] = 1
            else:
                first[i] += 1
        
        for j in t:
            if j not in second:
                second[j] = 1
            else:
                second[j] += 1

        return first == second