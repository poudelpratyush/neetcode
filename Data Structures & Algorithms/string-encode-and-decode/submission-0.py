class Solution:

    def encode(self, strs: List[str]) -> str:
        en = ""
        for i in strs:
            en += str(len(i)) + "#" + i
        return en

    def decode(self, s: str) -> List[str]:
        # 4#neet4#code4#love3#you
        de = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            #l = 4
            #j+1 = 2
            de.append(s[j+1:j+1+length])
            i = int(j+1+length)
        return de
                
