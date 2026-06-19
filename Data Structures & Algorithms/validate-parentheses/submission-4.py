class Solution:
    def isValid(self, s: str) -> bool:
        """
            
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
