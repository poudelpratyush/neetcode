from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedS = "".join(sorted(s))
            # sorts the string first to for example ['a', 'e', 't']
            # then makes it back into a string with the "".join
            res[sortedS].append(s)


        return list(res.values())
