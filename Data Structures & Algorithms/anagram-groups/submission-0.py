from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # O(n*m)
        anagram_dict = defaultdict(list)

        for s in strs: # O(n)
            curr = [0] * 26
            for j in s: # O(m) 
                curr[ord(j) - ord('a')] += 1
            key = tuple(curr)
            anagram_dict[key].append(s)
        return list(anagram_dict.values())
        
