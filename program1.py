class Solution(object):
    def isValid(self, s):
        
        # Stack to keep track of opening brackets
        stack = []
        
        # Dictionary to map closing to opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        # Iterate through each character in the string
        for char in s:
            # If it's a closing bracket
            if char in bracket_map:
                # Pop the top of the stack if not empty, else assign a dummy value
                top_element = stack.pop() if stack else '#'
                
                # If the mapping for the closing bracket doesn't match the stack's top, return False
                if bracket_map[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)
        
        # If the stack is empty, all brackets were matched correctly
        return not stack
    pass








    



  

