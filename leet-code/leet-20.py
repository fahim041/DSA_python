# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# Input: s = "(]"
# Output: false

# Input: s = "()[]{}"
# Output: true

def isValid(s):
    stack = []
    hashMap = {")" : "(", "}" : "{", "]" : "["}

    for char in s:
        if char in hashMap:
            if stack and stack[-1] == hashMap[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
    return len(stack) == 0