class Solution:
    def isValid(self, s: str) -> bool:
        """
            We care about order so we will be using a stack. For each closing char found we check if the top item
            in the stack matches its opening and pop the item if not we will return false.
        """
        
        closing = {"}":"{", "]":"[", ")":"("}
        s_stack = []
        for char in s:
            closing_char = closing.get(char, 0)
            if closing_char == 0:
                s_stack.append(char)
            else:
                if not s_stack or s_stack.pop() != closing_char:
                    return False
                 
        return len(s_stack) == 0
