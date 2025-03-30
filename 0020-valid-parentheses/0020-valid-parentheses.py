class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 

        pairs = {")" : "(", "}" : "{", "]" : "["}

        for i in s:
            if i == "[" or i == "(" or i == "{":
                stack.append(i)
            
            else:
                if not stack:
                    return False
                elif  stack[-1] != pairs[i]:
                    return False
                    
                else:
                    stack.pop()
        
        if stack:
            return False
        return True
                
             