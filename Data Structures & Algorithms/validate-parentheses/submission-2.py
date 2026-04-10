class Solution:
    def isValid(self, s: str) -> bool:
        ch = []

        for b in s:
            if (b == '{' or b == '(' or b == '['):
                ch.append(b)
            elif (len(ch) == 0):
                return False
            elif (b == '}'):
                if (ch[-1] != '{'):
                    return False
                ch.pop()
            elif (b == ')'):
                if (ch[-1] != '('):
                    return False
                ch.pop()
            elif (b == ']'):
                if (ch[-1] != '['):
                    return False
                ch.pop()


        if (len(ch) == 0):
            return True
        return False