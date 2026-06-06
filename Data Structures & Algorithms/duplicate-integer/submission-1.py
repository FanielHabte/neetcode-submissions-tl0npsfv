class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Loop through the values
        # for each ith check it that number is in [i+1:]

        unique = set(nums)

        if len(unique) < len(nums):
            return True
        else:
            return False