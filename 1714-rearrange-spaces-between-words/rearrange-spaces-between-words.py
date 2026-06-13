class Solution:
    def reorderSpaces(self, text: str) -> str:
        numSpaces = 0
        words = []
        currWord = []
        for c in text:
            if c is ' ':
                numSpaces += 1
                if len(currWord) > 0:
                    words.append(''.join(currWord))
                    currWord = []
            else:
                currWord.append(c)
        if len(currWord) > 0:
            words.append(''.join(currWord))

        if len(words) == 1:
            balancesSpaces = 0
            extraSpaces = numSpaces
        else:
            balancedSpaces = numSpaces // (len(words) - 1)
            extraSpaces = numSpaces % (len(words) - 1)

        

        result = []
        for w in range(len(words)):
            result.append(words[w])
            if w is not len(words) - 1:
                for i in range(balancedSpaces):
                    result.append(' ')
        
        for i in range(extraSpaces):
            result.append(' ')
        
        return ''.join(result)