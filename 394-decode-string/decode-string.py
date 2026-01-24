class Solution:
    def decodeString(self, s: str) -> str:
        # Neetcode soluton - using a stack
        stack = []

        for i in range(len(s)):
            # find the first ']' and work backwards
            if s[i] != ']':
                stack.append(s[i])
            else:
                substr = ''
                while stack[-1] != '[':
                    substr = stack.pop() + substr
                stack.pop() # get rid of the '['

                # read in the number
                k = ''
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack += (substr * int(k))
        
        return "".join(stack)
                



















        # # MY SOLUTION
        # def isNumber(char: str) -> bool:
        #     return ord('0') <= ord(char) <= ord('9')
        
        # def repeatString(num: int, input: str) -> str:
        #     # print('repeat string called', input)
        #     result = ''
        #     for i in range(num):
        #         result += input
        #     # print('result from repeat', result)
        #     return result

        # result = ''
        # i = 0
        # number = ''
        # currentString = ''
        
        # # base case
        # # when we encounter a close bracket for the beginning open bracket

        # while i < len(input):
        #     if isNumber(input[i]):                
        #         # read in the number
        #         while isNumber(input[i]) and i < len(input):
        #             number += input[i]
        #             i += 1
        #         i += 1 # skip the '['
        #         print('processing number', number)
        #         bracketLvl = 1
        #         while i < len(input):
        #             if input[i] == '[':
        #                 bracketLvl += 1
        #             elif input[i] == ']':
        #                 bracketLvl -= 1
        #                 if bracketLvl == 0:
        #                     i+=1
        #                     break # skip the original closing ']'
        #             currentString += input[i]
        #             i+=1
        #         # print('parsed string', currentString, i)
        #         currentString = self.decodeString(currentString)
        #         # flush it out to result, and reset 
        #         if currentString != '':
        #             # print("result before", result)
        #             result += repeatString(int(number), currentString)
        #             # print("after",result)

        #             currentString = ''
        #             number = ''
        #     else:
        #         result += input[i]
        #         i += 1
        
        # if number != '':
        #     result += repeatString(int(number), currentString)

        # return result


# number = 3
# currentString = 'a2[c]b3[d]'
# i = 2
# j = 12
# bracketLvl = 0
# 3[a2[c]b3[d]]

# 3
# [
#     a
#     2
#     [
#         c
#     ]

# ]
# aaa
