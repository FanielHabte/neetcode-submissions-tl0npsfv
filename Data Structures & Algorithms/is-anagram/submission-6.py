class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Overall Algorithm
        # 1. put each individual char and increment its count as value
        # 2. get/put each indivdual char and decrement its count as value
        
        char_count = {}
        # check the lengths of each string
        if len(s) != len(t):
            return False

        # increment a count of each char to the dict
        for i in range(len(s)):
            char_count[s[i]] = char_count.get(s[i], 0) + 1

        # decrement a count of each char to the dict
        for i in range(len(s)):
            char_count[t[i]] = char_count.get(t[i], 0) - 1
            # if the char count is less than 0 then there was no value
            if char_count[t[i]] < 0:
                return False

        return True


