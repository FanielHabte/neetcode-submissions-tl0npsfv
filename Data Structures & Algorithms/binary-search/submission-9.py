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

            # right of the mid
            if target > nums[mid]:
                left = mid + 1
            # left of the mid
            elif target < nums[mid]:
                right = mid - 1
            # equals to
            else:
                return mid
                
        return -1