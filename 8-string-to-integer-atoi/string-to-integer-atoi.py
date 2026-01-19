class Solution:
    def myAtoi(self, s: str) -> int:

        def isNumber(s: str) -> bool:
            return ord('0') <= ord(s) <= ord('9')
        
        def isLetter(s:str) -> bool:
            return ord('a') <= ord(s.lower()) <= ord('z')

        currNum = ''
        seenPositive = False
        seenNegative = False
        for c in s:
            if isNumber(c):
                if currNum == '0':
                    currNum = c
                else:
                    currNum = currNum + c
            elif isLetter(c):
                break
            elif c == ' ':
                if currNum != '' or seenPositive or seenNegative:
                    break
                else:
                    continue
            elif c == '-':
                if currNum != '' or seenNegative:
                        break
                seenNegative = True
            elif c == '+':
                if currNum != '' or seenPositive:
                    break
                seenPositive = True
            elif c == '.':
                break
            
        
        if currNum == '' or (seenPositive and seenNegative):
            return 0


        

        print(currNum)
        if seenNegative:
            if -int(currNum) < -2**31:
                return -2**31
        else:
            if int(currNum) > 2**31-1:
                return 2**31-1
        return -int(currNum) if seenNegative else int(currNum)
