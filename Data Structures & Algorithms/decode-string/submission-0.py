class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        currentnum = 0
        currentstring=""
        for ch in s:
            if ch.isdigit():
                currentnum = currentnum * 10 + int(ch)
            elif ch =='[':
                stack.append((currentstring,currentnum))
                currentstring = ""
                currentnum = 0
            elif ch ==']':
                previousstring,repeat = stack.pop()
                currentstring = previousstring +currentstring * repeat
            else:
                currentstring += ch
        return currentstring