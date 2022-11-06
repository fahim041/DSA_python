def validP(s):
    stack = []
    hashMap = {")":"(", "}":"{", "]":"["}

    for char in s:
        if char in hashMap:
            if stack and stack[-1] == hashMap[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
    return len(stack) == 0

print(validP("{([{}])}"))


