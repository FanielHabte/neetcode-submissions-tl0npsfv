class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_dict = dict()
        t_dict = dict()

        if len(s) != len(t):
            return False

        for char in s:
            s_dict[char] = s_dict.get(char, 0) + 1

        for char in t:
            if char not in s_dict:
                return False
            else:
                t_dict[char] = t_dict.get(char, 0) + 1

                if t_dict[char] > s_dict[char]:
                    return False
        return True



