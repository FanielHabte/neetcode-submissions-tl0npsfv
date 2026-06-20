class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
            1. if exists return its index if not return -1
            2. should not be a linear search
            3. orders are sorted from left to right
        """

        """
        Algorithm is to start from the middle and then check is the number is to right or 
        left and do this recursively until the number is found. We will need to have 2 pointer to know the range of the number that we check

        Each pointer should move to the side where the number lives
        """

        left, right = 0, len(nums) -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1