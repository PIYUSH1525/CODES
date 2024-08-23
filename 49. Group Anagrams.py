import collections
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            key = tuple(count)
            d[key].append(s)
            # d[tuple(count)].append(s)
        return list(d.values())
        # "d.values()"


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = Solution()
result = result.groupAnagrams(strs)
print(result)
