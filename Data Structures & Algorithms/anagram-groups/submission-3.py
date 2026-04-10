class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a hashmap
        # create a return list

        # loop through each string in strs
        # for each of them create an array of 26 zeros
        # loop through each character in the given string
        # fill in the values at the index of the character 
        # make that array to a tuple and make it a key in our hashmap
        # for each value in the hashmap add it to our return list
        # return the list

        res = defaultdict(list)
        for s in strs:
            check = [0] * 26
            for c in s:
                check[ord(c) - ord('a')] += 1
            res[tuple(check)].append(s)

        return list(res.values())