from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            strKey = [0] * 26
            for c in s:
                strKey[ord(c) - ord ("a")] += 1
            res[tuple(strKey)].append(s)
        
        return list(res.values())
             