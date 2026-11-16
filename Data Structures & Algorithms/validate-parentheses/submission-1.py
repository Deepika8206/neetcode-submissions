class Solution:
    def isValid(self, s: str) -> bool:
        pair = {']':'[' , ')':'(' , '}':'{'}
        stack = []
        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if not stack or stack.pop() != pair[ch]:
                    return False
        return len(stack) == 0
        
            