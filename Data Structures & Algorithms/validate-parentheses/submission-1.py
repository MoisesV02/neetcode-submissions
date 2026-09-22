class Solution:
    def isValid(self, s: str) -> bool:
        s.strip()
        closingStack = []
        hashmap = {')' : '(', ']' : '[', '}' : '{'}
        for char in s:
            if( char not in hashmap.keys()):
                closingStack.append(char)

            elif (char in hashmap and bool(closingStack) and (closingStack[-1] == hashmap[char])):
                closingStack.pop()
                

            else:
                return False

        if (not bool(closingStack)):
            return True

        return False