class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set(nums)
        for x in nums:
            print(x)
        return len(seen)!= len(nums)