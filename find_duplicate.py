from collections import Counter

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counter_dict = dict(Counter(nums))
        counter_dict = {key:value for key, value in counter_dict.items() if value > 1}
        for key, value in counter_dict.items():
            return key
