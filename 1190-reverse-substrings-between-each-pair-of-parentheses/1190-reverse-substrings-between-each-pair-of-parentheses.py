class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        i=0
        while i<len(s):
            if s[i]==')':
                temp=''
                while stack[-1]!='(':
                    temp+=stack.pop()
                stack.pop()
                # print(temp,temp[::-1])
                stack.extend(list(temp))
            else:   
                stack.append(s[i])
            i+=1
        return ''.join(stack)

    