class Solution:
    def isPalindrome(self, s: str) -> bool:
        lp = 0
        rp = len(s)-1
        while lp < rp:
            # move left pointer to the right if char is not alpha numeric
            while lp < rp and not s[lp].isalnum():
                lp+=1
            # move right pointer in words if the char is not alpha numeric
            while lp < rp and not s[rp].isalnum():
                rp-=1
            # check if right and left char are equal
            if s[lp].lower() != s[rp].lower():
                return False
            # move the pointer in-wards
            lp+=1
            rp-=1
        return True

