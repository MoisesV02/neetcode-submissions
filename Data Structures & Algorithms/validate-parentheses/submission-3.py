class Solution:
    def isValid(self, s: str) -> bool:
        #Removes whitespace from ends of string
        s.strip()
        closingStack = []
        hashmap = {')' : '(', ']' : '[', '}' : '{'}

        #Iterate through every character in s
        for char in s:

            #Checks that char is not a key of the dictionary to be able to append the character to the stack
            if( char not in hashmap.keys()):
                closingStack.append(char)

            #If char is a closing bracket, remove the top element
            #If the stack isn't empty & it matches the closing bracket
            elif (bool(closingStack) and (closingStack[-1] == hashmap[char])):
                closingStack.pop()
                
            #Otherwise, the brackets don't match
            else:
                return False

        #If the stack is empty at the end, then it is balanced
        if (not bool(closingStack)):
            return True

        return False