class Solution:
    def isValid(self, s: str) -> bool:
        """
            Brut force: 
                Hash map to keep track of the char and count of them. Then we check if the inverse that element has the same 
                count
        """
        if len(s) == 1:
            return False

        closing = {"}": "{", "]": "[", ")": "("}
        s_stack = []
        for i in range(len(s)):
            closing_char = closing.get(s[i], 0)

            if closing_char == 0:
                s_stack.append(s[i])
            else:
                if not s_stack or s_stack[-1] != closing_char:
                    return False
                s_stack.pop()
        return len(s_stack) == 0