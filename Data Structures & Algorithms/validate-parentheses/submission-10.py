class Solution:
    def isValid(self, s: str) -> bool:
        """
            We care about order so we will be using a stack. For each closing char found we check if the top item
            in the stack matches its opening and pop the item if not we will return false.
        """
        
        # dict that hold the mapping of closind and opening char
        char_dict = {"]":"[", "}":"{", ")":"("}
        char_stack = []

        # check if the str has char
        if len(s) <= 1:
            return False


        for char in s:
            # if its a closing character
            if not char in char_dict:
                char_stack.append(char)
            else: # pop the last value and compare
                # if top value not equal to poped value then return False
                if not char_stack or char_dict[char] != char_stack.pop():
                    return False
        return len(char_stack) == 0

