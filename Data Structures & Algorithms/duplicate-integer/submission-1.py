class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        for i in range(len(nums)-1):
            if nums[i] ^ nums[i+1] == 0:
                return True
        return False

