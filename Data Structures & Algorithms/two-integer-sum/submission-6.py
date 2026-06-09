from operator import itemgetter

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # check is number at opposite position are > or < the target
        # if greater pull your righ pointer to the left 
        # if less than  pull your left pointer to the right

        right_pointer = -1
        left_pointer = 0
        nums_pv_list = [{"position": i, "value": nums[i]} for i in range(len(nums))]

        if target < 0:
            nums_pv_list.sort(key=itemgetter("value"), reverse=True)
        else:
            nums_pv_list.sort(key=itemgetter("value"))

        while left_pointer > right_pointer:
            left_item = nums_pv_list[left_pointer]
            right_item = nums_pv_list[right_pointer]
            value = left_item.get("value", 0) + right_item.get("value", 0)

            if target < 0:
                if value > target:
                    left_pointer += 1
                if value < target:
                    right_pointer -= 1
            else:
                if value < target:
                    left_pointer += 1
                if value > target:
                    right_pointer -= 1
            if value == target:
                if left_item.get("position", 0) < right_item.get("position", 0):
                    return[left_item.get("position"), right_item.get("position")]
                else:
                    return[right_item.get("position"), left_item.get("position")]



                