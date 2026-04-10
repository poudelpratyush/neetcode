class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s

        return res
        
        # res = "5#hello5#world"
        # O(n)

    def decode(self, s: str) -> List[str]:
       resArr = []
       i = 0
       while (i != len(s)):
            j = i
            while (s[j] != "#"):
                j += 1
            count = int(s[i: j])
            resStr = s[j+1: j + 1 + count]
            resArr.append(resStr)
            i = j + 1 + count
       return resArr