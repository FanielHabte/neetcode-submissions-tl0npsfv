class Solution:
    def isPalindrome(self, s: str) -> bool:
        # iterate for the length of the string
        clean_string = ""
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isdigit():
                clean_string += s[i].lower()
            i += 1

        rp = -1
        for i in range(len(clean_string)):
            if clean_string[i] == clean_string[rp]:
                i+=1
                rp-=1
            else:
                return False
        return True
