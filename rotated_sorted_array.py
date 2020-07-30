class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return dict(zip(nums, range(0, len(nums)))).get(target) if target in set(nums) else -1
