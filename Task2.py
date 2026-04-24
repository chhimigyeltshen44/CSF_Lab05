def is_balanced(expression):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    
    for char in expression:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack or stack.pop() != pairs[char]:
                return "Not Balanced"
    
    return "Balanced" if not stack else "Not Balanced" 

print(is_balanced("(a+b)*(c+d)")) 
print(is_balanced("(a+b)* (c+d"))  