from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ann = defaultdict(list)
        for str in strs:
            sorted_str = ''.join(sorted(str))
            ann[sorted_str].append(str)
        return ann.values()
