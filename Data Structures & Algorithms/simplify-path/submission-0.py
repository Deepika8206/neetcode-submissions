class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for paths in path.split('/'):
            if paths == '' or paths ==  '.':
                continue
            elif paths == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(paths)
        return '/' + '/'.join(stack)