class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        count_dict = dict()

        if len(s) != len(t):
            return False

        for char in s:
            count_dict[char] = count_dict.get(char, 0) + 1

        for char in t:
            if char not in count_dict:
                return False

            count_dict[char] -= 1
            if count_dict[char] < 0 :
                return False
                
        return True



