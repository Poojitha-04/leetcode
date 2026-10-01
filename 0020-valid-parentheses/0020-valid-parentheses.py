class Solution:
    def isValid(self, s: str) -> bool:
        parantheses={'}':'{',']':'[',')':'('}
        stack=[]
        for i in s:
            if i=='[' or i=='(' or i=='{':
                stack.append(i)
            elif stack:
                if stack[-1]==parantheses.get(i):
                    stack.pop()
                else:
                    return False
            else:
                return False
        if stack:
            return False
        else:
            return True


        