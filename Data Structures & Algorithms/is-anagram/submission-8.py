class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s = "racecar", t = "carrace"
        # count if the strings are equal
        # if no return False
        # if yes
        # make hashmap for s
        # make hashmap for t
        # return the comparison of the hashmap

        if len(s) != len(t):
            return False
        sDict = {}
        tDict = {}
        for i in range(len(s)):
            sDict[s[i]] = 1 + sDict.get(s[i], 0)
            tDict[t[i]] = 1 + tDict.get(t[i], 0)
        return sDict == tDict