from operator import itemgetter

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # diff_dict holds the differece of n and target
        diff_dict = dict()
        for i in range(len(nums)):
            diff = target - nums[i] 
            # check if the diff is in the dict
            if diff in diff_dict:
                # key = diff and value is index
                # the value from the dict is always less as we found it earlier
                return [diff_dict[diff], i]
            # add the number to the dict
            diff_dict[nums[i]] = i

