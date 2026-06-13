class Solution:
    def reverseVowels(self, s: str) -> str:
        
        def isVowel(s: str) -> bool:
            vowels = {'a','e','i','o','u'}
            return s.lower()  in vowels
        
        l = 0
        r = len(s) - 1
        while l <= r:
            if not isVowel(s[l]):
                l += 1
                continue
            if not isVowel(s[r]):
                r -= 1
                continue

            temp = s[l]
            s = s[:l] + s[r] + s[l+1:] #replace left
            s = s[:r] + temp + s[r+1:] #replace right
            l += 1
            r -= 1
        
        return s
            
                