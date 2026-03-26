
def validParentheses(s):
    stack = []  # stack to keep track of opening brackets

    closeToOpen = {')': '(', '}': '{', ']': '['}  
    # mapping of closing bracket → corresponding opening bracket

    for c in s:  # iterate through each character in the string
        if c in closeToOpen:  # check if current char is a closing bracket
            if stack and stack[-1] == closeToOpen[c]:
                # if stack is not empty AND top matches expected opening bracket
                stack.pop()  # valid pair → remove the opening bracket
            else:
                return False  # mismatch or no opening bracket → invalid
        else:
            stack.append(c)  # if opening bracket → push onto stack

    return True if not stack else False  
# valid if stack is empty (all brackets matched), else invalid

print(validParentheses("([{}])"))