class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {'(':')', '[':']', '{':'}'}

        for char in s:
            if char in map:
                stack.append(map[char])

            else:
                if not stack or stack.pop() != char:
                    return False


        return len(stack)==0
            
