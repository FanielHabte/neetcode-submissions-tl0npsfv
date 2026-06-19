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
        left_pointer = 0
        right_pointer = len(nums) -1

        while left_pointer <= right_pointer:
            mid = (left_pointer + right_pointer) // 2
            if nums[mid] <  target:
                left_pointer = mid + 1
            elif nums[mid] >  target:
                right_pointer = mid - 1
            elif nums[mid] == target:
                return mid

        return -1