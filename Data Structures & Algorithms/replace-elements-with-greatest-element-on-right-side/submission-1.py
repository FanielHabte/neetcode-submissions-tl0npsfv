class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # iterate through the array
        # 0 - len
        for i in range(len(arr)-1):
            # assume that the next number if the biggest
            max = arr[i+1]
            for j in range(i+1, len(arr)):
                # check if the jth number if greater that my initial next number
                if arr[j] > max:
                    # if yes replace it max with jth number
                    max = arr[j]
            arr[i] = max
        arr[-1] = -1

        return arr
            # from ith number to the end check and get the max number