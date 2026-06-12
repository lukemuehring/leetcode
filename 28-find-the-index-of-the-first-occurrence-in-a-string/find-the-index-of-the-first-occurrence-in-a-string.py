class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        result = -1
        i = 0
        while i < len(haystack):
            if haystack[i] == needle[0]:
                result = i
                allMatched = True
                for j in range(len(needle)):
                    indexToCheck = i + j
                    if indexToCheck >= len(haystack):
                        return -1
                    if haystack[indexToCheck] != needle[j]:
                        allMatched = False
                        break
                if allMatched:
                    return result
            i += 1
        
        return -1