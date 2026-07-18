from collections import defaultdict, Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        res = defaultdict(list)
        for i, s in enumerate(strs):
            print(s)
            s_w = "".join(sorted(s))
            res[s_w].append(s)
        print(res.values())
        return list(res.values())
        """
        result = defaultdict(list)
        for word in strs:
            count = [0]*26
            for ch in word:
                ind = ord(ch) - ord('a')
                count[ind] +=  1
            result[tuple(count)].append(word)
        print(list(result.values()))
        return list(result.values())
