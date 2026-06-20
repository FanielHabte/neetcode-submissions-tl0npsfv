class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # char counter dict
        count_dict = dict()

        # return false if length don't match
        if len(s) != len(t):
            return False

        # increment the count by 1
        for char in s:
            count_dict[char] = count_dict.get(char, 0) + 1

        # decrement the count by 1
        for char in t:
            if char not in count_dict:
                return False

            count_dict[char] -= 1
            # break and return False of count goes below 0
            if count_dict[char] < 0 :
                return False

        # if everything works return True
        return True



