class Solution:
    def isValid(self, s: str) -> bool:
        s.strip()
        openingStack = []
        hashmap = {')' : '(', ']' : '[', '}' : '{'}
        for char in s:
            if( char not in hashmap.keys()):
                openingStack.append(char)

            elif (char in hashmap and bool(openingStack) and (openingStack[-1] == hashmap[char])):
                openingStack.pop()
                

            else:
                return False

        if (not bool(openingStack)):
            return True

        return False