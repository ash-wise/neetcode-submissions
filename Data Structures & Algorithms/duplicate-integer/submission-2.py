class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set(nums)
        if len(nums) != len(seen):
            print(seen)
        return len(seen) < len(nums)