class Solution:
    def minWindow(self, s: str, t: str) -> str:

        tHash = {}
        for c in t:
            tHash[c] = 1 + tHash.get(c, 0)
        
        need = len(tHash)
        have = 0

        result = ''

        window = {}
        l,r = 0,0 
        while r < len(s):
            c = s[r]
            window[c] = 1 + window.get(c,0)

            if c in tHash and window[c] == tHash[c]:
                have += 1
            
            while have == need:
                if result == '':
                    result = s[l:r+1]
                elif len(result) > r-l+1:
                    result = s[l:r+1]

                # pop left while have == need
                window[s[l]] = window[s[l]] - 1
                if s[l] in tHash and window[s[l]] < tHash[s[l]]:
                    have -= 1
                l += 1
            
            r += 1
        
        return result
